#!/usr/bin/python3
"""This module contains the defination of the class BaseGeometry."""


class BaseGeometry:
    """ BaseGeometry: under construction"""

    def area(self):
        """ area : not implemented yet"""
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


class Rectangle (BaseGeometry):
    """Rectangle: Class
    This class defines a rectangle object

    This is documentation for the constructor method.

    Args:
        width (int): The width of the triangle object.
        height (int): The height of the triangle object.

    Attributes:
        No Atrributes.
    """

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
