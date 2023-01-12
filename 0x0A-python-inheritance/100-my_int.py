#!/usr/bin/python3
""" 100-my_int: Module.
This module contains the defination of the class MyInt.

Classes:
    MyInt:
        This class defines a structure for MyInt objects.
"""


class MyInt(int):
    """ MyInt: Class
    This class defines a structure for MyInt objects.
    """

    def __eq__(self, other):
        return (not (not (self > other) and not (self < other)))

    def __ne__(self, other):
        return (not (self > other) and not (self < other))
