from unittest.mock import MagicMock

import pandas as pd
import pytest
import pytest_mock
from pandas.core.frame import DataFrame

import takehome
from takehome import transform


def test_version() -> None:
    assert takehome.__version__ == "0.1.0"


def test_when_row_is_missing_fields() -> None:
    # TODO: try and build what we can instead of failing on any missing fields
    with pytest.raises(KeyError):
        row = {}
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
