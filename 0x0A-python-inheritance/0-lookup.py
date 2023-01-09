#!/usr/bin/python3
"""
This is a documentation for the moduel '0-lookup.py'

This module contains a function that extract information on
attributes of an class or instane of an class.

Functions:
    lookup(obj) : returns a list of attributes of an object/Class.
"""


def lookup(obj):
    """ lookup : function.
    This function returns a list of attributes of a class or
    instance of a class.

    Args:
        obj(int): The object to return the list of attributes for.

    Return:
        A list of attributes of obj.
    """
    return (dir(obj))
