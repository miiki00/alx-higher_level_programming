#!/usr/bin/python3
""" 10-square: Module
This module contains the defination of the class Square.

Classes:
    Square: The defination for Square objects.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square: Class
    This class defines the structure of a Sqaure object.

    This is a documentation for the constructor method.

    Args:
        size (int): The size of the square object.

    Attributes:
        No attribtes.
    """

    def __init__(self, size):
        # validating input.
        self.integer_validator("size", size)

        super().__init__(size, size)
        self.__size = size

    def area(self):
        """ area: Method
        This method calculates the area of a square object.

        Args:
            No Arguments.

        Return:
            The area of the Square object.
        """
        return (self.__size ** 2)
