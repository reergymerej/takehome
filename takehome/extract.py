import pandas as pd


def get_input_data(input_path: str) -> pd.DataFrame:
    return pd.read_parquet(input_path)
