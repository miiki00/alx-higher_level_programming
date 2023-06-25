#!/usr/bin/python3

"""Module: square.py
Contains defination for a Square object.

Classes:
    Square:
        Contains defination of a square object.
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square: Defination of a Square object.

    Attributes:

    This is documentation for the constructor method of this class.

    Args:
        size(int): The height and width of the square.
        x(optional: int): The x axis position of the square.
        y(optional: int): The y axis position of the square.
        id(optional: int): Unique id of the square object.
    """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def update(self, *args, **kwargs):
        """
        update: updates attributes of instance.

        Args:
            1st: id
            2nd: size
            3rd: x
            4th: y
          or keyworded:
            id (int): Unique id to identify the object.
            size (int): The height and width to update the rectangle
                        object with.
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
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                pass

    def to_dictionary(self):
        """
        to_dictionary: Return the dictionary representation of instance
                       of Square class.

        Args:
            None.

        Return:
            The dictionary representation of the object.
        """

        keys = ["id", "size", "x", "y"]
        to_dict = {}
        for i in keys:
            to_dict[i] = self.__getattribute__(i)
        return (to_dict)

    def __str__(self):
        """
        __str__: returns representation of the square object.

        Args:
            None.

        Return:
            String representation of the square object.
        """
        st_format = f"[{type(self).__name__}] ({self.id}) {self.x}/{self.y}\
 - {self.width}"
        return (st_format)

    @property
    def size(self):
        """size : property.
        getter property for the private instance attributes __width and
        __height.

        Args:
            No arguments.

        Return:
            The width==height of the self rectangle object.
        """
        return (self.width)

    @size.setter
    def size(self, value):
        """size: property.
        setter property for the privated instance attributes __width
        and __height.

        Args:
            value (int): The value to set to the private instance attribute.
                         __widht and __height.

        Reuturn:
            None.
        """
        self.width = value
        self.height = value
