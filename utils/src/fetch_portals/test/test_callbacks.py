# Copyright 2020 Open Knowledge Brasil

# Use of this source code is governed by an MIT-style
# license that can be found in the LICENSE file or at
# https://opensource.org/licenses/MIT.

"""Tests callback functions.

This module contains test cases for checking whether the callback functions
defined in the `callbacks.py`_ file are working as expected.
"""

from datetime import datetime, timedelta, timezone

import pytest

from ...models import PortalCapture
from ..callbacks import _autogen_version_notes, to_kaggle


@pytest.fixture
def mock_captures():
    """Creates a list of fake records to process and/or save."""
    captures = [
        PortalCapture(
            ibge_code=2600807,
            initial_url=(
                "http://netuse.inf.br/altinho_pm/portaltransparencia/"
                + "index.php?link=6"
            ),
            final_url=(
                "http://netuse.inf.br/altinho_pm/portaltransparencia/"
                + "index.php?link=6"
            ),
            method="HEAD",
            attempts=1,
            request_time=datetime.now(timezone.utc),
            waiting_time=timedelta(seconds=1.1),
            ssl_valid=True,
            status=200,
            message="OK",
        ),
        PortalCapture(
            ibge_code=4200754,
            initial_url=(
                "https://diariomunicipal.sc.gov.br/site/"
                + "?r=site/index&q=cod_entidade%3A13"
            ),
            final_url=(
                "https://diariomunicipal.sc.gov.br/site/"
                + "?r=site/index&q=cod_entidade%3A13"
            ),
            method="HEAD",
            attempts=1,
            request_time=datetime.now(timezone.utc),
            waiting_time=timedelta(seconds=0.92),
            ssl_valid=True,
            status=200,
            message="OK",
        ),
    ]

    return captures


def test_autogen_version_notes():
    """Tests generating a default version note message."""
    expected_notes = {
        "create": "Create example.csv",
        "append": "Add records to example.csv",
        "update": "Update example.csv",
    }
    for operation, expected_note in expected_notes.items():
        version_note = _autogen_version_notes("example.csv", operation)
        assert version_note == expected_note


def test_to_kaggle(mock_captures, mock_kaggle_dataset, kaggle_api):
    """Tests saving some records to Kaggle"""
    to_kaggle(
        mock_captures,
        dataset=mock_kaggle_dataset,
        dest_file="example.csv",
    )
    file_list = kaggle_api.dataset_list_files(mock_kaggle_dataset)
    assert "example.csv" in [str(datafile) for datafile in file_list.files]
