# Copyright 2020 Open Knowledge Brasil

# Use of this source code is governed by an MIT-style
# license that can be found in the LICENSE file or at
# https://opensource.org/licenses/MIT.


from ...models import Portal, PortalList
from ..sources import get_portals_from_census


def test_get_portals_from_census() -> None:
    """Test getting a list of official gazettes portals from the QD census."""
    portals = get_portals_from_census()
    assert len(portals) >= 326  # there are at least 324 mapped portals
    assert isinstance(portals, PortalList)
    for portal in portals:
        assert isinstance(portal, Portal)
        # assert len(portal.ibge_code) == 7
        assert len(portal.url.host) > 5
