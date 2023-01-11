#!/usr/bin/python3
"""
This module contains function that help to obtain information
about a given variable or instance of class.
Classes:
    No class.
Functions:
    is_kind_of_class(obj, a_class):
        checks if obj is from a_class or inherited from.
"""


def is_kind_of_class(obj, a_class):
    """
    This function tells if obj is instance of a_class or inherited from.
    Args:
        obj(any): instance of any class you want to chekc.
        a_class(class): The class you want to check if obj is instance of
                        or inherited from.
    Return:
        True (obj is instance of a_class or inherited from),
        False (obj is not instance of a_class).
    """
    return (issubclass(type(obj), a_class))
