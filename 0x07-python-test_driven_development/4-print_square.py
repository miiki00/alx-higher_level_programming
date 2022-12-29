#!/usr/bin/python3
"""
This module contains function that deals with geometry.

Functions:
    print_square(size):
        prints a square size of size with the characters '#'
"""


def print_square(size):
    """ print_square : function

    prints a Square object with '#' characters on a given position by
    it's attribute.
    Args:
        size (int): The size of the square to print.

    Return:
        for test purposes there is a return statment that return the
        square that is going to be print if you wnat it for any reason
        you can uncomment it but by default it does not return anything.
    """
    toPrint = ""

    if type(size) not in [int, float]:
        raise TypeError("size must be an integer")
    if type(size) is float:
        if size < 0:
            raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    size = int(size)

    for i in range(size):
        if i != size - 1:
            toPrint += '#' * size + '\n'
        else:
            toPrint += '#' * size
    if size != 0:
        print(toPrint)
        # if you want you can uncommnet the return statment.
        return (toPrint)
