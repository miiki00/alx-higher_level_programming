#!/usr/bin/python3
"""
This module contains a functioni that appends a string to
a text file.

Functions:
    append_file(filename="", text=""):
        Appends the text 'text' to the file named filename.
"""


def append_write(filename="", text=""):
    """append_file: function.
    This function writes the text 'text' to the file named filename.

    Args:
        filename(str): The file to the write the text to.
        text(str): the string to write to the file.

    Return:
        The number of characters written
    """

    if not filename:
        return (0)
    with open(filename, mode='a', encoding='utf-8') as myFile:
        return (myFile.write(text))
