import pandas as pd


def get_input_data(input_path: str) -> pd.DataFrame:
    return pd.read_parquet(input_path)


# TODO read from args
# source = './inputs'
# print(get_input_data(source))
