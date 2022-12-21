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

    def __lt__(self, other):

        """ __lt__

        handles less than comparasion betwwen two Square
        objecs based on their area.
        Args:
            Other (:obj: Square): the other Square object to compare it
            with

        Return:
            True if self is < other
            False if self is >= other
        """

        return (self.area() < other.area())

    def __le__(self, other):

        """ __le__

        handles less than or is equals to comparasion betwwen two Square
        objecs based on their area.
        Args:
            Other (:obj: Square): the other Square object to compare it
            with

        Return:
            True if self is <= other
            False if self is > other
        """

        return (bool(self.area() <= other.area()))

    def __eq__(self, other):

        """ __eq__

        handles is equals to comparasion betwwen two Square
        objecs based on their area.
        Args:
            Other (:obj: Square): the other Square object to compare it
            with

        Return:
            True if self is = other
            False if self is != other
        """

        return (bool(self.area() == other.area()))

    def __ne__(self, other):

        """ __ne__

        handles not equal to comparasion betwwen two Square
        objecs based on their area.
        Args:
            Other (:obj: Square): the other Square object to compare it
            with

        Return:
            True if self is != other
            False if self is = other
        """

        return (bool(self.area() != other.area()))

    def __gt__(self, other):

        """ __gt__

        handles greater thancomparasion betwwen two Square
        objecs based on their area.
        Args:
            Other (:obj: Square): the other Square object to compare it
            with

        Return:
            True if self is > other
            False if self is <= other
        """

        self_area = self.area
        other_area = other.area

        return (bool(self.area() > other.area()))

    def __ge__(self, other):

        """ __ge__

        handles greater than or equal to comparasion betwwen two Square
        objecs based on their area.
        Args:
            Other (:obj: Square): the other Square object to compare it
            with

        Return:
            True if self is >= other
            False if self is < other
        """

        self_area = self.area
        other_area = other.area

        return (bool(self.area() >= other.area()))
