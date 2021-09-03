import pandas as pd

def get_input_data(input_path: str) -> pd.DataFrame:
    return pd.read_parquet(input_path)

def make_patients_from_df(df: pd.DataFrame) -> bool:
    ## How do we map a dataframe?
    for _, row in df.iterrows():
        make_patient_from_row(row)
    return True

def make_patient_from_row(row: pd.Series) -> None:
    print(type(row))
    print(row['name'])
    return 