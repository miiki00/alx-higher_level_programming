#!/usr/bin/python3
"""
This module contains the defination of the class BaseGeometry.

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
        """Validate a parameter as an integer.
        Args:
            name (str): The name of the parameter.
            value (int): The parameter to validate.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
