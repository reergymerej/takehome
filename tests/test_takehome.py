import json
from typing import Dict
from unittest.mock import MagicMock, patch

import pytest

import takehome
from takehome import load, transform
from takehome.extract import get_input_data


def test_version() -> None:
    assert takehome.__version__ == "0.1.0"


def test_when_row_is_missing_fields() -> None:
    # TODO: try and build what we can instead of failing on any missing fields
    with pytest.raises(KeyError):
        row: Dict[None, None] = {}
        transform.row_to_patient(row)


def test_parquet_is_read_from_provided_path() -> None:
    with patch("pandas.read_parquet") as mock:
        input_path = "some/sweet/path/"
        get_input_data(input_path)
        mock.assert_called_once_with(input_path)


def test_write_file_opens_correctly() -> None:
    from unittest.mock import mock_open, patch

    with patch("builtins.open", mock_open()) as mock_file_open:
        destination = "some/destination.file"
        content = "sweet"
        load.write_file(destination, content)
        mock_file_open.assert_called_with(destination, "w")


def test_loading_json_to_dir_create_missing_dir() -> None:
    with patch("os.path.isdir") as mock_isdir:
        mock_isdir.return_value = False
        with patch("os.mkdir") as mock_mkdir:
            json_list = [json.dumps({})]
            destination = "some/path/"
            load.load(json_list, destination)
            mock_mkdir.assert_called_with(destination)


def test_loading_json_to_dir_when_dir_exists() -> None:
    with patch("os.path.isdir") as mock_isdir:
        mock_isdir.return_value = True
        with patch("os.mkdir") as mock_mkdir:
            json_list = [
                json.dumps({"foo": "bar"}),
            ]
            destination = "some/path/"
            load.write_file = MagicMock()
            load.load(json_list, destination)
            mock_mkdir.assert_not_called()
