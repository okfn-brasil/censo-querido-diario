# Copyright 2020 Open Knowledge Brasil

# Use of this source code is governed by an MIT-style
# license that can be found in the LICENSE file or at
# https://opensource.org/licenses/MIT.

"""Functions to fetch official gazette portals statuses and contents.

This module contains functions developed as a part of the `Censo Querido
Diário`_ effort, in order to periodically fetch the contents and monitor the
service availability of portals containing the official gazettes for the 5.526
brazilian municipalities.

The Censo Querido Diário is a collaborative effort to push forward the
disclosure of public information embodied in official publications.
Contributions to this initiative are more than welcome. Check our
`contribution guidelines`_ (in portuguese) to learn the various ways you can
support the project.

.. _Censo Querido Diário:
    https://censo.ok.org.br/sobre/

.. _contribution guidelines:
    https://github.com/okfn-brasil/censo-querido-diario/blob/main/CONTRIBUTING.MD
"""

import asyncio
import logging

# from itertools import chain
from typing import List

from .models import FetchMode, PortalList


async def _gather_responses(
    portals: PortalList,
    mode: FetchMode = "ping",
    max_retries: int = 3,
    timeout: float = 10.0,
):
    """Orchestrates asynchronous requests to official gazettes portals.

    Parameters:
        portals: A `PortalList` instance to be fetched.
        mode: How to fetch the portals. ``mode="ping"`` fetches only the
            portals' status codes and request metadate. ``mode="capture"`` also
            captures the portals' source code.
    """

    logging.info("Preparing fetch tasks...")

    portals = PortalList(portals)

    http_method: str
    if mode == "ping":
        http_method = "HEAD"
    elif mode == "source":
        http_method = "GET"

    task_list: List = list()

    for subset in portals.by_domain():
        task: asyncio.Task = asyncio.create_task(
            subset.fetch_all(
                method=http_method,
                max_retries=max_retries,
                timeout=timeout,
            )
        )
        task_list.append(task)

    return await asyncio.gather(*task_list)


def fetch_portals(
    portals: PortalList,
    mode: FetchMode = "ping",
    max_retries: int = 3,
    timeout: float = 10.0,
):
    """Orchestrates asynchronous requests to official gazettes portals.

    Parameters:
        portals: A `PortalList` instance to be fetched.
        mode: How to fetch the portals. ``mode="ping"`` fetches only the
            portals' status codes and request metadate. ``mode="capture"`` also
            captures the portals' source code.
    """

    results = list()

    task_list = asyncio.run(
        _gather_responses(portals, mode, max_retries, timeout)
    )

    for task_results in task_list:
        for result in task_results:
            results.append(result)

    return results
