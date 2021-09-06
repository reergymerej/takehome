import os
import uuid
from typing import List


def write_file(destination: str, content: str) -> None:
    # TODO: consider overwrite
    f = open(destination, "w")
    f.write(content)
    f.close()


def load(json_list: List[str], destination: str = "./output") -> None:
    if not os.path.isdir(destination):
        os.mkdir(destination)

    for item in json_list:
        patient_uuid = str(uuid.uuid4())
        filename = f"{patient_uuid}.json"
        filepath = os.path.join(destination, filename)
        # TODO: handle errors and go to next
        # TODO: report results, show processed and unprocessed to allow for
        # cleanup and another attempt
        write_file(filepath, item)
