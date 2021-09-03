from pandas.core.frame import DataFrame
from takehome.go import get_input_data, make_patients_from_df
import takehome
from unittest.mock import MagicMock
import pytest_mock 

def test_version() -> None:
    assert takehome.__version__ == "0.1.0"


def test_get_input_data() -> None:
    assert type(get_input_data('./inputs')) == DataFrame
    

def test_make_patients_from_df() -> None:
    # TODO: use fixtures
    df = get_input_data('./inputs')

    make_patients_from_df = MagicMock()

    result = make_patients_from_df(df)
    make_patients_from_df.assert_called_once_with(df)

    # assert True == True