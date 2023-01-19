#!/usr/bin/python3
"""
This module contains a function that deserializes a json string
from a file and return the python object.

Functions:
    load_from_json_file(filename):
        deserializes a json string from a file and return the python object.
"""
import json


def load_from_json_file(filename):
    """load_from_json_file: function
    This function deserializes a json string from a file into
    a python object.

    Args:
        filename(str): The name of the json file to read from.

    Return:
        The deserialized object.
    """

    with open(filename, encoding='utf-8') as myFile:
        return (json.load(myFile))
