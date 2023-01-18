#!/usr/bin/python3
"""
This Module contains a functiont that reads a file
and print the content to the standard out put.

Functions:
    read_file(filename=""):
        Reads a file named filename and prints it to stdout.
"""


def read_file(filename=""):
    """ read_file: function
    This function read a file and prints it's content
    to the standard output.

    Args:
        filename (str): The name of the file to read.

    Return:
        None.
    """
    if not filename:
        return
    with open(filename, encoding='utf-8') as myFile:
        print(myFile.read(), end="")
