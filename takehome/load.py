"""
    ## Load
    From memory, move data into destination.
"""

import os
import typing
import uuid


def write_file(destination: str, content: str) -> None:
    # TODO: consider overwrite
    f = open(destination, "w")
    f.write(content)
    f.close()


def load(json_list: typing.List[str], destination="./output") -> None:
    if not os.path.isdir(destination):
        os.mkdir(destination)

    for item in json_list:
        patient_uuid = str(uuid.uuid4())
        filename = f"{patient_uuid}.json"
        filepath = os.path.join(destination, filename)
        write_file(filepath, item)
