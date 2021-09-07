from takehome.extract import get_input_data
from typing import Dict

import pandas as pd
import pytest
import json

import takehome
from takehome import transform, load

from unittest.mock import MagicMock, patch


# def test_init_pajamas():
#     from takehome import takehome
# 
#     with mock.patch.object(takehome, "main", return_value=42):
#         with mock.patch.object(takehome, "__name__", "__main__"):
#             with mock.patch.object(takehome.sys, 'exit') as mock_exit:
#                 takehome.init()
#                 assert mock_exit.call_args[0][0] == 42

def test_version() -> None:
    assert takehome.__version__ == "0.1.0"


def test_when_row_is_missing_fields() -> None:
    # TODO: try and build what we can instead of failing on any missing fields
    with pytest.raises(KeyError):
        row: Dict[None, None] = {}
        transform.row_to_patient(row)


@pytest.fixture
def dummy_row() -> pd.Series:
    return pd.Series(
        {
            "name": "Richard Clarke",
            "sex": "M",
            "address": "533 Sarah Summit\nCharlesport, TN 87961",
            "email": "iramirez@yahoo.com",
            "birthdate": "1913-05-23",
            "ssn": "074-22-3263",
        }
    )


def test_fixture() -> None:
    row = dummy_row
    expected = row
    actual = row
    print(row)
    assert expected == actual


def test_row_to_patient() -> None:
    row = dummy_row
    expected = transform.row_to_patient(row)
    actual = transform.row_to_patient(row)
    assert expected == actual


# extract

@patch('pandas.read_parquet')
def test_parquet_is_read_from_provided_path(mock) -> None:
    input_path = 'some/sweet/path/'
    get_input_data(input_path)
    mock.assert_called_once_with(input_path)

# load

def test_write_file_opens_correctly() -> None:
    from unittest.mock import patch, mock_open
    with patch("builtins.open", mock_open()) as mock_file_open:
        destination = 'some/destination.file'
        content = 'sweet'
        load.write_file(destination, content)
        mock_file_open.assert_called_with(destination, 'w')

def test_loading_json_to_dir_create_missing_dir() -> None:
    with patch("os.path.isdir") as mock_isdir:
        mock_isdir.return_value = False
        with patch("os.mkdir") as mock_mkdir:
            json_list = []
            destination = 'some/path/'
            load.load(json_list, destination)
            mock_mkdir.assert_called_with(destination)

def test_loading_json_to_dir_when_dir_exists() -> None:
    with patch("os.path.isdir") as mock_isdir:
        mock_isdir.return_value = True
        with patch("os.mkdir") as mock_mkdir:
            json_list = [
                json.dumps({"foo": "bar"}),
            ]
            destination = 'some/path/'
            load.write_file = MagicMock()
            load.load(json_list, destination)
            mock_mkdir.assert_not_called()
