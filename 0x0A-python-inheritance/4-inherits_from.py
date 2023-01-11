#!/usr/bin/python3
"""
This module contains function that help to obtain information
about a given variable or instance of class.
Classes:
    No class.
Functions:
    iherits_from(obj, a_class):
        check if obj is instance of a class that is inherited directly
        or indirectly from a_class but not instance of a_class itself.
"""


def inherits_from(obj, a_class):
    """
    This function tells if obj is instance of a_class.

    Args:
        obj(any): instance of any class you want to chekc.
        a_class(class): The class you want to check if obj is instance of.

    Return:
        True (obj is instance of a class that is inherited from a_class),
        False (obj is not instance of a class that is inherited from a_class).
    """
    return (type(obj) is not a_class and issubclass(type(obj), a_class))
