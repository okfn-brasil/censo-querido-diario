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
from typing import cast, Final, List, Optional

from dotenv import load_dotenv

from .callbacks import to_kaggle
from .fetchers import fetch_portals
from .models import (
    AcceptedCallback,
    AcceptedSource,
    ExistingBehavior,
    FetchMode,
    LogLevel,
    PathLike,
    PortalCapture,
)
from .sources import get_portals_from_census

# get configurations from environment variables, or use defaults
script_path: Path = Path(os.path.abspath(__file__))
load_dotenv(os.path.join(script_path.parents[2], ".env"))


# load settings from environment, or use defaults
SOURCE: Final = os.getenv("FETCHPORTALS_SOURCE", "census")
MODE: Final = os.getenv("FETCHPORTALS_MODE", "ping")
CALLBACK: Final = os.getenv("FETCHPORTALS_CALLBACK", None)
LOCAL_DIR: Final = os.getenv("FETCHPORTALS_LOCALDIR", None)
EXISTING: Final = os.getenv("FETCHPORTALS_EXISTING", "replace")
MAX_RETRIES: Final = int(os.getenv("FETCHPORTALS_MAX_RETRIES", 3))
TIMEOUT: Final = float(os.getenv("FETCHPORTALS_TIMEOUT", 10.0))
LOG_LEVEL: Final = os.getenv("FETCHPORTALS_LOG_LEVEL", "warning")


def main(
    source: AcceptedSource = cast(AcceptedSource, SOURCE),
    mode: FetchMode = cast(FetchMode, MODE),
    callback: Optional[AcceptedCallback] = cast(
        Optional[AcceptedCallback], CALLBACK
    ),
    local_dir: Optional[PathLike] = LOCAL_DIR,
    existing: ExistingBehavior = cast(ExistingBehavior, EXISTING),
    max_retries: int = MAX_RETRIES,
    timeout: float = TIMEOUT,
    log_level: LogLevel = cast(LogLevel, LOG_LEVEL),
) -> None:
    """Main program entry point."""
    # init logs
    logging.basicConfig(
        format="%(asctime)s %(message)s",
        level=getattr(logging, log_level.upper())
    )

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
