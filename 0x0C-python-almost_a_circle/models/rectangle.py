#!/usr/bin/python3

"""Module: rectangel.py
Contains the defination of a rectangel object.

Classes:
    Rectangle:
        Defination of a rectnagle object.
"""


from models.base import Base


class Rectangle(Base):
    """ Rectangle: class.

    This module contains a definations of A rectangle objects
    and methods to act upon them.

    This is a documenation for the constructor method of Recntangle.

    Args:
        width (int): The widht to instantiate the rectangle object with.
        height (int): The height to instantiate the rectangle object with.
        x (optional: int): The postion of the rectangle in x axis.
        y (optional: int): The postion of the rectangle in y asix.
        id (optional: int): Unique id to identify the object.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        """
        area: mehtod to caculate the area of a rectangle object.

        Args:
            None.

        Return:
            The area of the rectangle object.
        """
        return (self.width * self.height)

    def display(self):
        """
        display : display the rectange on the terminal.

        Args:
            None.

        Return:
            None.
        """
        char = "#"
        for i in range(self.y):
            print("\n", end="")

        for i in range(self.height):
            print(" " * self.x + char * self.width)

    def update(self, *args, **kwargs):
        """
        update: updates attributes of instance.

        Args:
            1st: id
            2nd: width
            3rd: height
            4th: x
            5th: y
          or keyworded:
            id (int): Unique id to identify the object.
            width (int): The widht to instantiate the rectangle object with.
            height (int): The height to instantiate the rectangle object with.
            x (int): The postion of the rectangle in x axis.
            y (int): The postion of the rectangle in y asix.

        Return:
            None.
        """
        if len(args) == 0:
            for key, value in kwargs.items():
                self.__setattr__(key, value)
        else:
            try:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
            except IndexError:
                pass

    def to_dictionary(self):
        """
        to_dictionary: Return the dictionary representation of instance
                       of Rectangle class.

        Args:
            None.

        Return:
            The dictionary representation of the object.
        """

        keys = ["id", "width", "height", "x", "y"]
        to_dict = {}
        for i in keys:
            to_dict[i] = self.__getattribute__(i)
        return (to_dict)

    def __str__(self):
        """
        __str__: returns representation of the rctangle object.

        Args:
            None.

        Return:
            String representation of the rectangle object.
        """
        st_format = f"[{type(self).__name__}] ({self.id}) {self.x}/{self.y}\
 - {self.width}/{self.height}"
        return (st_format)

    @property
    def width(self):
        """Width : property.
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
        elif value < 1:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """height : property.
        getter property for the private instance attribute __height.

        Args:
            No arguments.

        Return:
            The height of the self rectangle object.
        """

        return (self.__height)

    @height.setter
    def height(self, value):
        """height: property.
        setter property for the privated instance attribute __height.

        Args:
            value (int): The value to set to the private instance attribute.
                         __height.

        Reuturn:
            None.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 1:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """x : property.
        getter property for the private instance attribute __x.

        Args:
            No arguments.

        Return:
            The x position of the self rectangle object.

        """
        return (self.__x)

    @x.setter
    def x(self, value):
        """x: property.
        setter property for the privated instance attribute __x.

        Args:
            value (int): The value to set to the private instance attribute.
                         __x.

        Reuturn:
            None.
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """y: property.
        getter property for the private instance attribute __y.

        Args:
            No arguments.

        Return:
            The y position of the self rectangle object.

        """
        return (self.__y)

    @y.setter
    def y(self, value):
        """y: property.
        setter property for the privated instance attribute __y.

        Args:
            value (int): The value to set to the private instance attribute.
                         __y.

        Reuturn:
            None.
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value
