#!/usr/bin/python3
"""
This module contains a function that serializes a python object
and write the json representation to a file.

Functions:
    save_to_json_file(my_obj, filename):
        Serializes a pyton object 'my_obj' and writes the
        json representation into a file named 'filename'.
"""
import json


def save_to_json_file(my_obj, filename):
    """save_to_json_file: function
    This function Serializes a pyton object 'my_obj' and writes the
    json representation into a file named 'filename'.

    Args:
        my_obj(any_object): The object to be serialized.
        filename(str): The name of the file to write the json
                       Representation of the object 'my_obj'.

    Return:
        None.
    """
    with open(filename, 'w', encoding='utf-8') as myFile:
        json.dump(my_obj, myFile)
