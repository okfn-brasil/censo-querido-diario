#!/usr/bin/env python3

# Copyright 2020 Open Knowledge Brasil

# Use of this source code is governed by an MIT-style
# license that can be found in the LICENSE file or at
# https://opensource.org/licenses/MIT.

"""Tests callback functions.

This module contains test cases for checking whether the callback functions
defined in the `callbacks.py`_ file are working as expected.
"""

import os
from tempfile import TemporaryDirectory

import pandas as pd

from ..main import main


def test_ping(capsys):
    """Tests pinging all portals in Querido Diario Census."""
    main(mode="ping", callback=None)
    out, err = capsys.readouterr()
    assert '"ibge_code": "2600807"' in out


def test_source(capsys):
    """Tests getting source codes for all portals in Querido Diario Census."""
    main(mode="source", callback=None)
    out, err = capsys.readouterr()
    assert '"ibge_code": "2600807"' in out
    assert "<html>" in out


def test_ping_to_kaggle(mock_kaggle_dataset, kaggle_api):
    """Tests saving pings to all portals in QD Census to Kaggle."""
    # copy original kaggle dataset config (that should not to be modified)
    previous_kaggle_dataset = os.getenv("KAGGLE_DATASET")
    previous_kaggle_file = os.getenv("KAGGLE_FILE")

    # upload data to mock dataset
    try:
        os.environ["KAGGLE_DATASET"] = mock_kaggle_dataset
        os.environ["KAGGLE_FILE"] = "test-ping.csv"
        main(mode="ping", callback="kaggle", existing="append")
        with TemporaryDirectory() as tmpdir:
            kaggle_api.dataset_download_file(
                mock_kaggle_dataset, os.environ["KAGGLE_FILE"], tmpdir
            )
            df = pd.read_csv(os.path.join(tmpdir, os.environ["KAGGLE_FILE"]))
            for col in [
                "ibge_code",
                "request_time",
                "waiting_time",
                "attempts",
                "initial_url",
                "final_url",
                "method",
                "ssl_valid",
                "status",
                "message",
                "level",
                "branch",
            ]:
                assert col in df.columns
            assert len(df.index) > 3
            assert "200" in df["status"].unique()
            assert "OK" in df["message"].unique()

    # reset kaggle dataset config to the original one
    finally:
        if previous_kaggle_dataset:
            os.environ["KAGGLE_DATASET"] = previous_kaggle_dataset
        else:
            del os.environ["KAGGLE_DATASET"]
        if previous_kaggle_file:
            os.environ["KAGGLE_FILE"] = previous_kaggle_file
        else:
            del os.environ["KAGGLE_FILE"]


def test_source_to_kaggle(mock_kaggle_dataset, kaggle_api):
    """Tests saving source codes for all portals in QD Census to Kaggle."""
    # copy original kaggle dataset config (that should not to be modified)
    previous_kaggle_dataset = os.getenv("KAGGLE_DATASET")
    previous_kaggle_file = os.getenv("KAGGLE_FILE")

    # upload data to mock dataset
    try:
        os.environ["KAGGLE_DATASET"] = mock_kaggle_dataset
        os.environ["KAGGLE_FILE"] = "test-source.csv"
        main(mode="source", callback="kaggle")
        with TemporaryDirectory() as tmpdir:
            kaggle_api.dataset_download_file(
                mock_kaggle_dataset, os.environ["KAGGLE_FILE"], tmpdir
            )
            try:
                df = pd.read_csv(
                    os.path.join(tmpdir, os.environ["KAGGLE_FILE"])
                )
            except FileNotFoundError:
                df = pd.read_csv(
                    os.path.join(tmpdir, os.environ["KAGGLE_FILE"] + ".zip")
                )
            for col in [
                "ibge_code",
                "request_time",
                "waiting_time",
                "attempts",
                "initial_url",
                "final_url",
                "method",
                "ssl_valid",
                "status",
                "message",
                "level",
                "branch",
            ]:
                assert col in df.columns
            assert len(df.index) > 3
            assert df["message"].apply(lambda msg: "<html>" in str(msg)).any()

    # reset kaggle dataset config to the original one
    finally:
        if previous_kaggle_dataset:
            os.environ["KAGGLE_DATASET"] = previous_kaggle_dataset
        else:
            del os.environ["KAGGLE_DATASET"]
        if previous_kaggle_file:
            os.environ["KAGGLE_FILE"] = previous_kaggle_file
        else:
            del os.environ["KAGGLE_FILE"]
