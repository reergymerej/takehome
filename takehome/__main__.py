from takehome.go import make_patients_from_df
import go
from pandas.core.frame import DataFrame

def do_it() -> bool:
    # TODO: make path dynamic
    input_path = './inputs'
    df = go.get_input_data(input_path)
    print(df)
    make_patients_from_df(df)
    return True

do_it()