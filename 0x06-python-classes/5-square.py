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
        self.size = size

    @property
    def size(self):
        """ size

        A getter method for the attribute size
        Args:
            no args

        Return:
            The value of the size attribute.
        """

        return (self.__size)

    @size.setter
    def size(self, value):
        """ size

        A setter method for the attribute size
        Args:
            Value (int) - the size of the square.

        Return
            None
        """

        if type(value) is int:
            if value >= 0:
                self.__size = value
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
        return (self.size ** 2)

    def my_print(self):
        """ my_print

        prints a Square object with '#' characters
        Args:
            no Arguments

        Return:
            None
        """

        for i in range(self.size):
            print('#' * self.size)
        if self.size == 0:
            print('')
