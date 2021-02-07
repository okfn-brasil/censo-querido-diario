# Copyright 2020 Open Knowledge Brasil

# Use of this source code is governed by an MIT-style
# license that can be found in the LICENSE file or at
# https://opensource.org/licenses/MIT.

"""Representations of concepts used by other utilities.

This module contains reusable types and classes that model both portals where
Brazilian official gazettes are published and their attributes.
"""

import itertools
import logging
import os
from asyncio.exceptions import TimeoutError
from collections import UserList
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from enum import Enum
from typing import Any, List, Literal, NewType, Optional, Set, Union

import aiohttp
from aiohttp import ClientConnectorCertificateError, ClientError, ClientTimeout
from yarl import URL

FetchMode = Literal["ping", "source"]
IbgeCode = NewType("IbgeCode", int)  # TODO: make it a UserString
LogLevel = Literal["error", "warn", "info", "debug"]
PathLike = Union[str, bytes, os.PathLike]


class GovernmentBranch(Enum):
    """An enumeration of government branches in Brazil."""

    EXECUTIVE = 1  # only the Executive branch is currently supported
    # LEGISLATIVE = 2
    # JUDICIAL = 3
    # ESSENTIAL_JUSTICE = 4


class GovernmentLevel(Enum):
    """An enumeration of government levels in Brazil."""

    # FEDERAL = 1
    # STATE = 2  # includes Federal District
    MUNICIPALITY = 3  # only Municipalities are currently supported


@dataclass
class Portal:
    """Representation of a portal that publishes local-level official gazettes."""

    ibge_code: IbgeCode
    url: URL
    branch: GovernmentBranch = GovernmentBranch.EXECUTIVE
    level: GovernmentLevel = GovernmentLevel.MUNICIPALITY


@dataclass
class PortalCapture:
    """Capture of an official gazette publication portal at a point in time."""

    ibge_code: IbgeCode
    request_time: datetime
    waiting_time: timedelta
    attempts: int
    initial_url: URL
    final_url: Optional[URL]
    method: Literal["GET", "POST"]
    ssl_valid: bool
    status: int
    message: str
    level: str = GovernmentLevel.MUNICIPALITY.name
    branch: str = GovernmentBranch.EXECUTIVE.name


class PortalList(UserList):
    """A list of official portals."""

    def by_domain(self) -> List["PortalList"]:
        """Separate a list of portals by their domains.

        This function creates a list populated with sets of unique portals that
        have all the same domain in their URLs.

        Parameters:
            portals: An iterable of `Portal` instances

        Returns:
            A list of `PortalList`s, one for each domain in the original
            instance.
        """

        logging.debug("Separating portals according to their domains...")

        # collect all unique domains
        domains = set(portal.url.host for portal in self.data)

        # iterate over domains and check which portals belong to them
        separated = list()
        for domain in domains:
            portals_in_domain = PortalList(
                portal for portal in self.data if portal.url.host == domain
            )

            separated.append(portals_in_domain)  # add to separated list

        return separated

    async def fetch_all(
        self,
        method: Literal["GET", "HEAD"] = "HEAD",
        timeout: float = 10.0,
        max_retries: int = 3,
    ) -> List[PortalCapture]:

        logging.info(f"Fetching {len(self.data)} portals ('{method}')...")

        # create an empty list of responses data and metadata
        responses: List[dict] = list()

        # remove url duplicates
        unique_urls: Set[URL] = set(portal.url for portal in self.data)

        client_timeout = ClientTimeout(total=timeout)

        async with aiohttp.ClientSession(
            timeout=client_timeout, trust_env=True
        ) as client:

            # iterate over portal URLs
            for url in unique_urls:

                # configure request
                ssl_valid: bool = True  # start assuming so

                # try fetching page
                attempt: int = 1
                while attempt <= max_retries:
                    try:
                        logging.info(
                            f"Sending request to <{url}> "
                            + f"({attempt}/{max_retries})..."
                        )
                        request_time: datetime = datetime.now(timezone.utc)

                        async with client.request(
                            method, url=str(url), verify_ssl=ssl_valid
                        ) as response:
                            time_elapsed: timedelta = (
                                datetime.now(timezone.utc) - request_time
                            )
                            final_url: Optional[URL] = response.url
                            response_status: int = response.status
                            if method == "GET":
                                message: Any = str(await response.text())
                            else:
                                message = response.reason
                            if not response.ok and attempt <= max_retries:
                                attempt += 1
                                continue

                    # Invalid SSL certificate; try again without verifying
                    except ClientConnectorCertificateError:
                        ssl_valid = False
                        if attempt < max_retries:
                            continue

                    # some other error; try again
                    except (ClientError, TimeoutError) as err:
                        time_elapsed = (
                            datetime.now(timezone.utc) - request_time
                        )
                        message = err.__str__
                        final_url = None
                        response_status = 999
                        if attempt < max_retries:
                            attempt += 1
                            continue

                    # record answer if it is OK or exceeded max tries
                    logging.info(response_status)
                    responses.append(
                        {
                            "initial_url": url,
                            "final_url": final_url,
                            "method": method,
                            "attempts": attempt,
                            "request_time": request_time,
                            "waiting_time": time_elapsed,
                            "ssl_valid": ssl_valid,
                            "status": response_status,
                            "message": message,
                        }
                    )
                    break

        # associate unique urls to portals
        captures: List[PortalCapture] = list()
        for portal, capture in itertools.product(self.data, responses):
            if portal.url == capture["initial_url"]:
                print(portal.url)
                captures.append(
                    PortalCapture(
                        ibge_code=portal.ibge_code,
                        level=portal.level.value,
                        branch=portal.branch.value,
                        **capture,
                    )
                )
        print(len(captures))
        return captures
