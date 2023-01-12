#!/usr/bin/python3
""" 8-rectangle : Module
This module contains the defination of the class
Rectangle.

Classes:
    Rectangle: Defines a rectangle object.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
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
        # validating inputs
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """ area: method.
        calculates the area of a rectangle object.

        Args:
            No arguments.


        Returns:
            The Area of the rectangle object self.
        """
        return (self.__width * self.__height)

    def __str__(self):
        """ __str__: magic method.
        This method handles the string representation of
        Rectangle object.

        Args:
            No arguments.

        Return:
            The string representation of the Rectangle object.
        """
        width = self.__width
        height = self.__height
        return ("[{}] {}/{}".format(type(self).__name__, width, height))
