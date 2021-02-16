# Copyright 2020 Open Knowledge Brasil

# Use of this source code is governed by an MIT-style
# license that can be found in the LICENSE file or at
# https://opensource.org/licenses/MIT.

"""Periodically check the availability of Official Gazettes portals.
"""

import logging

import azure.functions as func
from fetch_portals.main import main as fetch


def main(timer: func.TimerRequest):
    """Ping Querido Diario Census portals to check their availability."""
    logging.info(f"Starting function (past due {timer.past_due})")
    fetch(mode="ping", existing="append", callback="kaggle")
    logging.info("Finished checking portals from Census.")
