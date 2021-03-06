import os
import uuid
from typing import List


def write_file(destination: str, content: str) -> None:
    # We'll allow you to overwrite.
    f = open(destination, "w")
    f.write(content)
    f.close()


def load(json_list: List[str], destination: str) -> None:
    if not os.path.isdir(destination):
        os.mkdir(destination)

    for item in json_list:
        try:
            patient_uuid = str(uuid.uuid4())
            filename = f"{patient_uuid}.json"
            filepath = os.path.join(destination, filename)
            write_file(filepath, item)
        except:  # noqa: E722
            pass
            # If this were more robust, we'd handle this.

    # report results, show processed and unprocessed to allow for
    # cleanup and another attempt
