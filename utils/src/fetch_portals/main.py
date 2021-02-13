# Copyright 2020 Open Knowledge Brasil

# Use of this source code is governed by an MIT-style
# license that can be found in the LICENSE file or at
# https://opensource.org/licenses/MIT.

"""Main logic to capture data from official gazettes portals.

This module contains main logic to capture official gazette portals' status and
source code for Brazilian municipalities. developed as a part of the `Censo
Querido Diário`_ effort, in order to periodically fetch the contents and
monitor the service availability of portals containing the official gazettes
for the 5.526 brazilian municipalities.

The Censo Querido Diário is a collaborative effort to push forward the
disclosure of public information embodied in official publications.
Contributions to this initiative are more than welcome. Check our `contribution
guidelines`_ (in portuguese) to learn the various ways you can support the
project.

.. _Censo Querido Diário: https://censo.ok.org.br/sobre/

.. _contribution guidelines:
    https://github.com/okfn-brasil/censo-querido-diario/blob/main/CONTRIBUTING.MD
"""

import json
import logging
import os
import sys
from pathlib import Path
from typing import List, Optional

from dotenv import load_dotenv

from ..models import (AcceptedCallback, AcceptedSource, ExistingBehavior,
                      FetchMode, LogLevel, PathLike, PortalCapture)
from .callbacks import to_kaggle
from .fetchers import fetch_portals
from .sources import get_portals_from_census

# get configurations from environment variables, or use defaults
script_path: Path = Path(os.path.abspath(__file__))
load_dotenv(os.path.join(script_path.parents[2], ".env"))


def main(
    source: AcceptedSource = os.getenv("FETCHPORTALS_SOURCE", "census"),
    mode: FetchMode = os.getenv("FETCHPORTALS_MODE", "ping"),
    callback: Optional[AcceptedCallback] = os.getenv("FETCHPORTALS_CALLBACK"),
    local_dir: Optional[PathLike] = os.getenv("FETCHPORTALS_LOCALDIR"),
    existing: ExistingBehavior = os.getenv("FETCHPORTALS_EXISTING", "replace"),
    max_retries: int = os.getenv("FETCHPORTALS_MAX_RETRIES", 3),
    timeout: float = os.getenv("FETCHPORTALS_TIMEOUT", 10.0),
    log_level: LogLevel = os.getenv("FETCHPORTALS_LOG_LEVEL", "warn"),
) -> None:
    # init logs
    logging.basicConfig(format="%(asctime)s %(message)s", level=log_level)

    # get a list of portals
    if source == "census":
        portals = get_portals_from_census()
    else:
        raise ValueError(f"'{source}' is not a valid source.")

    # fetch them
    captures: List[PortalCapture] = fetch_portals(portals=portals, mode=mode)

    # save captured data
    if callback == "kaggle":  # save to a Kaggle dataset file
        try:
            assert "KAGGLE_USERNAME" in os.environ
            assert "KAGGLE_KEY" in os.environ
        except AssertionError:
            logging.error("Kaggle credentials not found in environment.")
            raise RuntimeError
        dest_dataset: str = os.environ["KAGGLE_DATASET"]
        dest_file: str = os.environ["KAGGLE_FILE"]
        to_kaggle(
            captures,
            dataset=dest_dataset,
            dest_file=dest_file,
            existing_behavior=existing,
            local_dir=local_dir,
        )

    # print to stdout (default)
    elif not callback:
        results_json: str = json.dumps(
            [capture.to_dict() for capture in captures],
            indent=4,
            sort_keys=True,
            separators=(",", ": "),
        ).replace("\\n", "\n")
        sys.stdout.write(results_json)

    # unimplemented callback
    else:
        raise ValueError(f"'{callback}' is not a valid callback.")


if __name__ == "__main__":
    main()
