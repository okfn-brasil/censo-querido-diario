# Copyright 2020 Open Knowledge Brasil

# Use of this source code is governed by an MIT-style
# license that can be found in the LICENSE file or at
# https://opensource.org/licenses/MIT.

"""Reusable Pytest fixtures for testing fetch_portals package."""

import json
import os
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Generator

import pytest
from dotenv import load_dotenv


@pytest.fixture(scope="session")
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


@pytest.fixture(scope="session")
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
