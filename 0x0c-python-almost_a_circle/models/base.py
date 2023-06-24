#!/usr/bin/python3
"""Module: base.py
This modules contains a class that define a Base for
other subclasses.

Classes:
    Base: Defines a base class for all subclasses under it.
"""


class Base:

    """Class: Base
    Base : The base class for all subclasses under it.

    Attributes:
        id (int): A unique id of the object being created.

    This is a documentation for the constructor method.

    Args:
        id (int): A unique id of the object being created.
    """

    __nb_objects = 0

    def __init__(self, id=None):

        if id is not None:
            self.id = id
        else:
            __nb_objects += 1
            self.id = __nb_objects
