# Copyright 2020 Open Knowledge Brasil

# Use of this source code is governed by an MIT-style
# license that can be found in the LICENSE file or at
# https://opensource.org/licenses/MIT.

"""Functions to interact with sources of official gazettes portals.

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

import logging
from typing import List

import numpy as np
import pandas as pd
from yarl import URL

from ..models import IbgeCode, Portal, PortalList


def get_portals_from_census() -> PortalList:
    """Get a list of official gazettes portals from Querido Diario Census data.

    Returns:
        A list of `Portal`_ objects, containing the official Id for the city
        and the portal URL.
    """

    logging.info("Getting census data...")

    # download census full data
    url: str = "https://censo.ok.org.br/get-data/"
    df_census: pd.DataFrame = pd.read_csv(url)

    # filter and process relevant data (cities geocodes and portal URLs)
    logging.debug("Processing portals information...")
    portals: List[Portal] = (
        pd.wide_to_long(df_census, "fonte", i="IBGE7", j="fonte_num", sep="_")
        .reset_index()
        .dropna()
        .apply(
            # FIXME: avoid "None" strings in url column
            lambda mun: Portal(
                ibge_code=IbgeCode(mun["IBGE7"]), url=URL(mun["fonte"])
            )
            if mun.fonte != "None"
            else np.nan,
            axis=1,
        )
        .dropna()
        .to_list()
    )

    portals = PortalList(portals)

    return portals
