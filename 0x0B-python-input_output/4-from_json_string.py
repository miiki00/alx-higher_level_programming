#!/usr/bin/python3
"""
This module contains a function that constructos
a python object from a json string(Deserialization).

Functions:
    from_json_string(my_str):
        Deserializes a json string.
"""
import json


def from_json_string(my_str):
    """
    This function constructs a python object from
    a json string(Deserialization).

    Args:
        my_str(str): The json string to deserialize.

    Return:
        The deserialized python object.
    """

    return (json.loads(my_str))
