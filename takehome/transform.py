import re
import datetime
import json
import typing

import pandas as pd
from fhir.resources import construct_fhir_element
from fhir.resources.patient import Patient


def transform(df: pd.DataFrame) -> typing.List[str]:
    json_list = []
    for _, row in df.iterrows():
        patient = row_to_patient(row)
        json_list.append(patient.json())
    return json_list

def get_gender(sex: str) -> typing.Literal[
    'female',
    'male',
    'other',
    'unknown',
    ]:
    if sex is None:
        return "unknown"
    elif sex is "M":
        return "male"
    elif sex is "F":
        return "female"
    else:
        return "other"

def get_ssn(ssn: str) -> str:
    return re.sub("[^0-9]", "", ssn)

def get_address(address: str):
    # https://www.hl7.org/fhir/datatypes.html#Address
    # We're not getting into the weeds parsing the address.  Just return
    # the text version.
    return construct_fhir_element('Address', {
        "text": address,
    })

def get_date(d: datetime.date) -> datetime.date:
    # https://www.hl7.org/fhir/datatypes.html#date
    return d

def get_name(name: str) -> str:
    # https://www.hl7.org/fhir/datatypes.html#HumanName
    return construct_fhir_element('HumanName', {
        "text": name,
    })

def get_email(email: str):
    # https://www.hl7.org/fhir/datatypes.html#ContactPoint
    return construct_fhir_element('ContactPoint', {
        "system": "email",
        "value": email,
    })

def get_ssn(ssn: str):
    # https://www.hl7.org/fhir/datatypes.html#Identifier
    return construct_fhir_element('Identifier', {
        # https://www.hl7.org/fhir/datatypes.html#CodeableConcept
        "type": construct_fhir_element('CodeableConcept', {
            "coding": [
                # https://www.hl7.org/fhir/datatypes.html#Coding
                construct_fhir_element('Coding', {
                    "system": "http://terminology.hl7.org/CodeSystem/v2-0203",
                    "code": "SS",
                }),
            ],
            "text": "Social Security number",
        }),
        "system": "http://hl7.org/fhir/sid/us-ssn",
        "value": ssn,
    })

def row_to_patient(dude) -> Patient:
    patient_dict = {
        "address": [
            get_address(dude['address']),
        ],

        "birthDate": get_date(dude['birthdate']),

        "resourceType": "Patient",

        "name": [
            get_name(dude["name"]),
        ],

        "gender": get_gender(dude["sex"]),

        "telecom": [
            get_email(dude['email']),
        ],

        "identifier": [
            get_ssn(dude['ssn']),
        ],
    }
    return Patient.parse_obj(patient_dict)
