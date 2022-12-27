#!/usr/bin/python3
"""
This module contains a function that adds two numbers.
Functions:
    add_integer(a, b=98):
        adds two integers.
"""


def add_integer(a, b=98):
    """
    This function adds two number a and b and
    returns the result.

    Args:
        a (int): The first number to add.
        b (int): The second number to add. if not supplied
                 defaults to 98.

    Return:
        The sum of the two numbers.
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return (int(a + b))
