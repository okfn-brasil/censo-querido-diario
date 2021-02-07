# Copyright 2020 Open Knowledge Brasil

# Use of this source code is governed by an MIT-style
# license that can be found in the LICENSE file or at
# https://opensource.org/licenses/MIT.

"""Tests callback functions.

This module contains test cases for checking whether the callback functions
defined in the `callbacks.py`_ file are working as expected.
"""


import json
import os
from datetime import datetime, timedelta, timezone
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Generator

import pytest
from dotenv import load_dotenv

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


@pytest.fixture(scope="module")
def kaggle_api() -> "KaggleApi":  # type: ignore  # noqa: F821
    """Initialize and authenticate connection to Kaggle API."""
    # get set kaggle credentials as environment variables
    script_path = Path(os.path.abspath(__file__))
    load_dotenv(os.path.join(script_path.parents[3], ".env"))

    # initialize api
    from kaggle.api.kaggle_api_extended import KaggleApi  # type: ignore

    api = KaggleApi()
    api.authenticate()

    return api


@pytest.fixture(scope="module")
def mock_kaggle_dataset(kaggle_api) -> Generator[str, None, None]:
    """Creates a Kaggle dataset for testing purposes.

    Note:
        There is currently no method for programatically removing a Kaggle
        dataset. Therefore, the user must manually delete the created dataset,
        located at ``https://kaggle.com/myuser/example`` (where ``myuser`` is
        the name of the Kaggle user provided through the ``KAGGLE_USER``
        environment variable).

    Yields:
        ID of the created dataset, in the format ``myuser/example``.
    """
    kaggle_user = os.environ["KAGGLE_USERNAME"]
    mock_data = """
        "fruit_name","fruit_color","fruit_number"
        apple,red,6
        banana,yellow,12
        plum,purple,5
        """
    try:
        tmpdir = TemporaryDirectory()
        metadata = {
            "title": "Example Dataset",
            "id": kaggle_user + "/example",
            "licenses": [{"name": "CC0-1.0"}],
        }
        with open(
            os.path.join(tmpdir.name, "datapackage.json"), "w"
        ) as meta_file:
            meta_json = json.dumps(metadata)
            meta_file.write(meta_json)
        with open(os.path.join(tmpdir.name, "example_fruits.csv"), "w") as f:
            f.write(mock_data)
        kaggle_api.dataset_create_new(tmpdir.name)
        yield metadata["id"]  # type: ignore
    finally:
        tmpdir.cleanup()


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
