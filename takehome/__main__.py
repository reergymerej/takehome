import extract
import load
import transform

import takehome.paths

if __name__ == "__main__":
    import sys

    args = sys.argv[1:]
    (source, destination) = takehome.paths.get_paths(args)
    df = extract.get_input_data(source)
    json_list = transform.transform(df)
    load.load(json_list, destination)
