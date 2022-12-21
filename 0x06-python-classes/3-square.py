#!/usr/bin/python3


""" 0-square
Contains a class that defines a square
"""


class Square:

    """ Square - A class that defines a square object.

    This is a description for the __init__ method
    Args:
        size (:obj: 'int', options): The size of the square.

    Attributes:
        __size (int): The size of the square.
    """

    def __init__(self, size=0):
        if type(size) is int:
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """ area

        Calculates the area of a Square instance
        Args:
            no arguments

        Return:
            The area of the Square instance
        """
        return (self.__size ** 2)
