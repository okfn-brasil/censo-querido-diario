# Copyright 2020 Open Knowledge Brasil

# Use of this source code is governed by an MIT-style
# license that can be found in the LICENSE file or at
# https://opensource.org/licenses/MIT.

"""Callback functions to save data fetched from official gazettes portals.

This module contains callback functions to process and/or save contents and
monitor the service availability of portals containing the official gazettes
for the 5.570 brazilian municipalities.
"""

import json
import logging
import os
from dataclasses import is_dataclass
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Any, Iterable, Literal, Optional, Union

import pandas as pd

from ..models import PathLike, PortalCapture


def _autogen_version_notes(
    dest_file: str, operation: Literal["create", "append", "update"]
) -> str:
    """Generate a default version note message.

    Parameters:
        dest_file: Destination file being written (or appended to).
        operation: Whether the file is being ``create``'d, ``append`'ed to or
            completely ``update``'d (replaced).
    """

    logging.warning(
        "Version notes not provided; a default message will be generated."
    )

    if operation == "create":
        version_notes = "Create " + dest_file
    elif operation == "append":
        version_notes = "Add records to " + dest_file
    elif operation == "update":
        version_notes = "Update " + dest_file

    return version_notes


def to_kaggle(
    data: Union[Iterable[Union[dict, PortalCapture]], pd.DataFrame],
    dataset: str,
    dest_file: str,
    existing_behavior: Literal["replace", "append", "skip"] = "replace",
    version_notes: Optional[str] = None,
    local_dir: Optional[PathLike] = None,
    delete_old_versions: bool = False,
) -> "DatasetNewVersionResponse":  # type: ignore  # noqa: F821
    """Write data to a destination dataset file in Kaggle.

    Parameters:
        data: Data to be uploaded to the dataset. Can be a pandas `DataFrame`_
            instance, or an iterable of dataclass objects or dictionaries.
        dataset: Kaggle dataset id, in the format ``<owner username>/<dataset
            name>``.
        dest_file: How to name the destination file in the dataset context.
        existing_behavior: What to do if the file already exists in the
            dataset.
        version_notes: A message describing what changes will be made to the
            dataset (optional; a default message will be generated if none was
            given).
        local_dir: A local directory where the dataset files will persist
            (optional; defaults to None).
        delete_old_versions: Whether to delete previous versions of the
            dataset that exist in Kaggle.

    Returns
        A `DatasetNewVersionResponse`_ instance with the new dataset version.

    .. _DataFrame: https://pandas.pydata.org/pandas-docs/stable/reference/
            frame.html
    .. _DatasetNewVersionResponse: https://github.com/Kaggle/kaggle-api/blob/
        89eb72dd811492c500839f65332f669cd839d2bc/kaggle/models/
        kaggle_models_extended.py#L150
    """

    from kaggle.api.kaggle_api_extended import KaggleApi  # type: ignore
    from kaggle.models.kaggle_models_extended import Metadata  # type: ignore

    # check data object type is supported
    if all(is_dataclass(record) for record in data) or all(
        isinstance(record, dict) for record in data
    ):
        data = pd.DataFrame(data)
    elif isinstance(data, pd.DataFrame):
        pass
    else:
        raise TypeError(
            "`data` parameter must be a list os Dataclass instances, a "
            + f"dictionary or a pandas DataFrame, not {type(data).__name__}."
        )

    logging.info(
        f"Uploading {len(data.index)} records to '{dest_file}' file in "
        + f"Kaggle's '{dataset}' dataset."
    )

    # authenticate Kaggle API
    logging.debug("Authenticating to Kaggle API...")
    api = KaggleApi()
    api.authenticate()

    # make sure dataset exists
    logging.debug("Searching dataset...")
    try:
        dataset_owner, dataset_name = dataset.split("/")
        matching_datasets = api.dataset_list(
            search=dataset_name, user=dataset_owner
        )
        assert dataset in [dataset.ref for dataset in matching_datasets]
    except AssertionError:
        # TODO: create dataset if it doesn't exist
        raise ValueError("The dataset does not exist.")

    # use the provided local (persistent) directory, or create a temporary one
    if not local_dir:
        tmpdir = TemporaryDirectory()
        data_dir: Any = tmpdir.name
        logging.debug(f"Creatd temporary directory: {data_dir}")
    else:
        data_dir = local_dir

    # get dataset metadata
    metafile = Path(data_dir, "datapackage.json")
    if not os.path.isfile(metafile):
        metadata_response = api.process_response(
            api.metadata_get_with_http_info(dataset_owner, dataset_name)
        )
        metadata = Metadata(metadata_response)
        with open(metafile, "w") as f:
            json.dump(metadata, f, indent=2, default=lambda o: o.__dict__)

    # download existing files
    # TODO: skip downloading unchanged files if they already exist locally
    # TODO: start downloading asynchronously while data is gathered
    api.dataset_download_files(dataset, path=data_dir, unzip=True)

    # write data file as CSV
    operation: Literal["create", "append", "update"]
    if os.path.isfile(Path(data_dir, dest_file)):
        if existing_behavior == "replace":
            operation = "update"
            data.to_csv(Path(data_dir, dest_file), mode="w")
        elif existing_behavior == "append":
            operation = "append"
            data.to_csv(Path(data_dir, dest_file), mode="a")
        elif existing_behavior == "skip":
            logging.error(f"File '{dest_file}' already exists. Skiped.")
            raise FileExistsError(
                "File already exists and behavior is set to `skip`."
            )
        else:
            raise ValueError(
                "`existing_behavior` argument must be one of "
                + f"`replace`, `append` or `skip` ('{existing_behavior}' "
                + "provided)."
            )
    else:
        operation = "create"
        data.to_csv(Path(data_dir, dest_file))

    # update metadata file
    try:
        api.dataset_metadata_update(dataset, data_dir)
    except KeyError:
        # BUG: KaggleApi's dataset_metadata_update() method references an
        # inexistent key for checking for errors. Just ignore it.
        pass

    # create a version notes message, if user hasn't provided one
    if not version_notes:
        version_notes = _autogen_version_notes(dest_file, operation)

    # upload data to Kaggle
    new_version = api.dataset_create_version(
        data_dir, version_notes, delete_old_versions=delete_old_versions
    )

    # clear temporary directory
    if not local_dir:
        tmpdir.cleanup()

    return new_version
