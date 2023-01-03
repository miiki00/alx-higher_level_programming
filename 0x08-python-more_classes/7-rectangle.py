#!/usr/bin/python3
""" 0-rectangel : module
contains a class defination and more things related to rectangles.

Class:
    Rectangle: used to define a Rectangle object.
"""


class Rectangle:
    """ Rectangle: class.

    This module contains a definations of A rectangle objects
    and methods to act upon them.

    Args:
        width (optional: int): The widht to instantiate the rectangle object
                               with if not provided it's defaulted to Zero(0).
        height (optional: int): The height  to instantiate the rectangle object
                                with if not provided it's defaulted to Zero().

    Attributes:
        width (int): widht of the rectangle object.
        height (int): height of the rectangle object.
        number_of_instances (int): number of instances of this class.
        print_symbol (any type): The symbol to print the square with.
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """ Width : property.
        getter property for the private instance attribute __width.

        Args:
            No arguments.

        Return:
            The width of the self rectangle object.
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """width: property.
        setter property for the privated instance attribute __width.

        Args:
            value (int): The value to set to the private instance attribute.
                         __widht.

        Reuturn:
            None.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ height : property.
        getter property for the private instance attribute __height.

        Args:
            No arguments.

        Return:
            The height of the self rectangle object.
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        """width: property.
        setter property for the privated instance attribute __height.

        Args:
            value (int): The value to set to the private instance attribute.
                         __height.

        Reuturn:
            None.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ area: method.
        calculates the area of a rectangle object.

        Args:
            No arguments.


        Returns:
            The Area of the rectangle object self.
        """
        return (self.width * self.height)

    def perimeter(self):
        """perimeter : method.
        calculates the perimeter of a rectangle object.

        Args:
            No arguments.

        Return:
            The perimeter of the rectangle object self.
        """
        if self.width == 0 or self.height == 0:
            return (0)
        return ((self.width * 2) + (self.height * 2))

    def __str__(self):
        """ __str__: private instance method.
        a private instance method that returnes a formated string
        representation of a rectangle object.

        Args:
            No arguments.

        Return:
            The formated string representation of a rectangle object self.
        """
        strRep = ''
        width = self.width
        height = self.height

        if width == 0 or height == 0:
            return (strRep)
        for i in range(height):
            strRep += str(self.print_symbol) * width
            if i < height - 1:
                strRep += '\n'
        return (strRep)

    def __repr__(self):
        """ __repr__: private instance method.
        a privated instance method that returns the code representation
        of the self rectangle object.

        Args:
            No arguments.

        Return:
            The ode representation of the self rectangle object.
        """
        return ('Rectangle({}, {})'.format(self.width, self.height))

    def __del__(self):
        """__del__ : privated instance method.
        This code is executed every time a Rectangle object is deleted.
        it prints a goodbye message.

        Args:
            No arguments.

        Return:
            None.
        """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
