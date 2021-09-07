from typing import List
import extract
import load
import transform

def get_source(args: List[str]) -> str:
    if len(args) > 0:
        return args[0] 
    return "./inputs"

def get_dest(args: List[str]) -> str:
    if len(args) > 1:
        return args[1] 
    return "./output"

if __name__ == "__main__":
    import sys
    args = sys.argv[1:]
    source = get_source(args)
    destination = get_dest(args)
    print(source, destination)

    df = extract.get_input_data(source)
    json_list = transform.transform(df)
    load.load(json_list, destination)
