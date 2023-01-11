#!/usr/bin/python3
"""
This module contains the defination of the class BaseGeometry.

Class:
    BaseGeometry:

Functions:
    No functions.
"""


class BaseGeometry:
    """ BaseGeometry: Class
    A BaseGeometry class defination.

    This is a documentation for the costructor method __init__.
    Args:
        No arguments.
    """

    def __init__(self):
        pass

    def area(self):
        """ area : method
        This method calculates the area of a BaseGeometry object

        Args:
            No arguments.

        Return:
            The area of the BaseGeometry object.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """integer_validator: method
        This methods wheater a value is a valid integer meaining '>=0'

        Args:
            name(str): The name of the var to asigne value to.
            value(int): The integer to assigne to name.

        Return:
            None.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
