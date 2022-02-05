"""
@Author: Maro Okegbero
@Date: 5th Feb 2021
"""
import json
from pprint import pprint


def humanize_type(value):
    """
    return the type in capitalized complete letters
    :param value:
    :return:
    """
    response = ""
    if isinstance(value, str):
        response = "STRING"

    if isinstance(value, int):
        response = "INTEGER"

    if isinstance(value, float):
        response = "NUMBER"

    if isinstance(value, dict):
        response = "OBJECT"

    if isinstance(value, bool):
        response = "BOOLEAN"

    if isinstance(value, list):
        response = "ENUM" if isinstance(value[0], str) else "ARRAY"

    return response


def prepare_dict(key, value):
    """
    return prepared dictionary object
    :param value:
    :param key:
    :return:
    """
    response = {"tag": "", "description": ""}
    value_type = humanize_type(value)
    response["type"] = value_type
    if value_type == "OBJECT":
        response["required"] = []
        response["properties"] = {}
        for k, v in value.items():
            print(k, "this is the k", k)
            response["properties"].update({k: prepare_dict(k, v)})
            response["required"].append(k)
    if value_type == "ARRAY":
        response["required"] = []
        response["items"] = {}
        print(value, "The vaalue..........")

        for k, v in value[0].items():
            response["items"].update({k: prepare_dict(k, v)})
            response["required"].append(k)

    return response


def sniffer(file=None):
    """
    snif JSON object and write sniffed object in to a sample.json file

    :return:
    """

    file_path = "data/example_input.json" if not file else file
    x = open(file_path)
    data = json.load(x)
    sniffed = dict()
    message = data.get("message")
    if message:
        for key, value in message.items():
            sniffed[key] = prepare_dict(key, value)

    pprint(sniffed)

    with open("sample.json", "w") as outfile:
        json.dump(sniffed, outfile)

    x.close()

    return sniffed
