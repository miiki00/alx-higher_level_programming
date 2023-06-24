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
