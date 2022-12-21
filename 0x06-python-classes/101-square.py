#!/usr/bin/python3


""" 0-square
Contains a class that defines a square
"""


class Square:

    """ Square - A class that defines a square object.

    This is a description for the __init__ method
    Args:
        size (:obj: 'int', optional): The size of the square.
        position (:obj: 'tuple', optional): The position of the square
        when printed

    Attributes:
        __size (int): The size of the square.
        __position (tupel): The position of the square when printed
    """

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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

        A setter method for the attribute size.
        If invalid value is passed to size a TypeError
        exception will be raised
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

    @property
    def position(self):

        """ position

        A getter method for the attribute position.
        Args:
            no Argumetns

        Return:
            The value of position attribute.
        """

        return (self.__position)

    @position.setter
    def position(self, value):

        """ position

        A setter methond for the attribute position.
        If invalid argument is passed a TypeError exception
        is raised.
        Args:
            Value (tupel) : a tupel with 2 positive integers

        Return:
            None
        """
        if type(value) is tuple:
            if len(value) == 2:
                if type(value[0]) is int and type(value[1]) is int:
                    if value[0] >= 0 and value[1] >= 0:
                        self.__position = value
                        return
        raise TypeError("position must be a tuple of 2 positive integers")

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

        prints a Square object with '#' characters on a given position by
        it's attribute.
        Args:
            no Arguments

        Return:
            None
        """

        if self.size != 0:
            cpy_position = self.position
            print('\n' * cpy_position[1], end='')
        for i in range(self.size):
            print(' ' * cpy_position[0], end='')
            print('#' * self.size)
        if self.size == 0:
            print('')

    def __str__(self):

        """ __str__
        A method that handles str call on Square objects
        Args:
            no Arguments

        Return:
            The format string of squareo drawn with '#' and
            the position of the square
            if the size of the square is 0 empty string is
            returned.
        """

        to_print = ''

        if self.size != 0:
            cpy_position = self.position
            to_print += '\n' * cpy_position[1]
        for i in range(self.size):
            to_print += ' ' * cpy_position[0]
            to_print += '#' * self.size
            if i != self.size - 1:
                to_print += '\n'
        return (to_print)
