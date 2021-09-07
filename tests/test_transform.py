import json
from typing import Literal, Union

import pandas as pd
import pytest

from takehome.transform import get_gender, transform

Gender = Literal["female", "male", "other", "unknown"]


@pytest.mark.parametrize(
    "sex, expected_result",
    [
        (None, "unknown"),
        ("M", "male"),
        ("F", "female"),
        ("?", "other"),
    ],
)
def test_get_gender(sex: Union[str, None], expected_result: Gender) -> None:
    assert get_gender(sex) == expected_result


def test_transform() -> None:
    fixture = {
        "name": "Richard Clarke",
        "sex": "M",
        "address": "533 Sarah Summit\nCharlesport, TN 87961",
        "email": "iramirez@yahoo.com",
        "birthdate": "1913-05-23",
        "ssn": "074-22-3263",
    }
    expected = [
        json.dumps(
            {
                "address": [{"text": "533 Sarah Summit\nCharlesport, TN 87961"}],
                "birthDate": "1913-05-23",
                "gender": "male",
                "identifier": [
                    {
                        "system": "http://hl7.org/fhir/sid/us-ssn",
                        "type": {
                            "coding": [
                                {
                                    "code": "SS",
                                    "system": "http://terminology.hl7.org/CodeSystem/v2-0203",
                                }
                            ],
                            "text": "Social Security number",
                        },
                        "value": "074223263",
                    }
                ],
                "name": [{"text": "Richard Clarke"}],
                "telecom": [{"system": "email", "value": "iramirez@yahoo.com"}],
                "resourceType": "Patient",
            }
        )
    ]
    df = pd.DataFrame(fixture, index=[0])
    actual = transform(df)
    assert actual == expected
