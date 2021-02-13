# Copyright 2020 Open Knowledge Brasil

# Use of this source code is governed by an MIT-style
# license that can be found in the LICENSE file or at
# https://opensource.org/licenses/MIT.

import asyncio
from typing import List, Set

import pytest
from httpx import URL

from ..fetchers import fetch_portals
from ..models import Portal, PortalCapture, PortalList


@pytest.fixture
def example_portals() -> PortalList:
    """Create a `PortalList`_ instance with a few official gazette portals."""

    # Altinho (PE)
    portal1: Portal = Portal(
        ibge_code=2600807,
        url=URL(
            "http://netuse.inf.br/altinho_pm/portaltransparencia/index.php?"
            + "link=6"
        ),
    )
    portal2: Portal = Portal(
        ibge_code=2600807, url=URL("http://www.diariomunicipal.com.br/amupe/")
    )

    # Alto Bela Vista (SC)
    portal3: Portal = Portal(
        ibge_code=4200754,
        url=URL(
            "https://diariomunicipal.sc.gov.br/site/"
            + "?r=site/index&q=cod_entidade%3A13"
        ),
    )

    # Anchieta (SC)
    portal4: Portal = Portal(
        ibge_code=4200804,
        url=URL(
            "https://diariomunicipal.sc.gov.br/site/"
            + "?r=site/index&q=cod_entidade%3A14"
        ),
    )

    # Angelim (PE)
    portal5: Portal = Portal(
        ibge_code=2601003,
        url=URL("http://www.diariomunicipal.com.br/amupe/pesquisar"),
    )
    portal6 = Portal(
        ibge_code=2601003,
        url=URL(
            "http://174.142.65.52:16444/transparencia/angelim/prefeitura/"
            + "legislacaomunicipal.faces"
        ),
    )
    portal7 = Portal(
        ibge_code=2601003,
        url=URL(
            "http://174.142.65.52:16444/transparencia/angelim/prefeitura/"
            + "outrosatos.faces"
        ),
    )

    return PortalList(
        [portal1, portal2, portal3, portal4, portal5, portal6, portal7]
    )


def test_split_by_domain(example_portals) -> None:
    """Tests spliting `PortalList`_s into instances with an unique domain each.
    """
    splitted: PortalList = example_portals.by_domain()
    for subset in splitted:
        domains: Set[str] = set(portal.url.host for portal in subset)
        assert len(domains) == 1


def test_head_subsets(example_portals) -> None:
    """Tests pinging subsets of a `PortalList`_ with unique domains."""
    subsets: PortalList = example_portals.by_domain()
    for subset in subsets:
        subset = PortalList(subset)
        captures: List[PortalCapture] = asyncio.run(
            subset.fetch_all(method="HEAD", timeout=30)
        )
        assert len(captures) == len(subset)
        for capture in captures:
            assert isinstance(capture, PortalCapture)


def test_get_subsets(example_portals) -> None:
    """Tests capturing subsets of a `PortalList`_ with unique domains."""
    subsets: PortalList = example_portals.by_domain()
    for subset in subsets:
        subset = PortalList(subset)
        captures: List[PortalCapture] = asyncio.run(
            subset.fetch_all(method="GET", timeout=30)
        )
        assert len(captures) == len(subset)
        for capture in captures:
            assert isinstance(capture, PortalCapture)


def test_orchestrate_pinging(example_portals) -> None:
    """Tests asynchronously pinging multiple portals."""
    captures: List[PortalCapture] = fetch_portals(example_portals, mode="ping")
    assert len(captures) == len(example_portals)
    for capture in captures:
        assert isinstance(capture, PortalCapture)


def test_orchestrate_sourcing(example_portals) -> None:
    """Tests asynchronously getting source code for multiple portals."""
    captures: List[PortalCapture] = fetch_portals(
        example_portals, mode="source"
    )
    assert len(captures) == len(example_portals)
    for capture in captures:
        assert isinstance(capture, PortalCapture)
