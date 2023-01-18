#!/usr/bin/python3
"""
This module contains a function that serializes a python
object to json string representaion.

Functions:
    to_json_string(my_obj):
        serializes a python object to json string representaion.
"""
import json


def to_json_string(my_ob):
    """to_json_string: function.
    This mehtod converst a python object into a json string
    representation(serialization).

    Args:
        my_obj(any_object): The object to serialize.

    Return:
        The json string representation of the object.
    """
    return json.dumps(my_ob)
