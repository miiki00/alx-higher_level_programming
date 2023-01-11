#!/usr/bin/python3
"""
This module contains function that help to obtain information
about a given variable or instance of class.

Classes:
    No class.
Functions:
    is_same_class(obj, a_class):
        This function tells if obj is instance of a_class.
"""


def is_same_class(obj, a_class):
    """
    This function tells if obj is instance of a_class.

    Args:
        obj(any): instance of any class you want to chekc.
        a_class(class): The class you want to check if obj is instance of.

    Return:
        True (obj is instance of a_class),
        False (obj is not instance of a_class).
    """
    return (type(obj) is a_class)
