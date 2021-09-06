import extract
import load
import transform

if __name__ == "__main__":
    # import sys
    # print(sys.argv)
    # TODO: get from args
    source = "./inputs"

    # extract
    df = extract.get_input_data(source)

    # transform
    json_list = transform.transform(df)

    # load
    load.load(json_list)
