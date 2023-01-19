#!/usr/bin/python3
"""
This module contains a function that reutnrs the dectionary description
of an instance of a class json serialization.

Functions:
    class_to_json(obj):
        reutnrs the dectionary description of an instance of a class
        json serialization.
"""


def class_to_json(obj):
    """class_to_json: function
    This function reutnrs the dectionary description of an
    instance of a class json serialization.

    Args:
        obj(any_object): The object to return the dictionary
                         representation for.
    """

    return (obj.__dict__)
