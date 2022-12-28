#!/usr/bin/python3
""" 3-say_my_name : module
This module contains a function that prints first and last name in a
formated way.

functions:
    say_my_name(first_name, last_name=""):
        Takes first and last name and prints it in this format.
            eg :- firts_name = "Your"
                  last_name = "Name"
            output will be like this:
                "My name is Your Name"
"""


def say_my_name(first_name, last_name=""):
    """ say_my_name : function
    This function prints the passed first and last name in a formated way.

    Args:
        first_name (str): Your first name.
        last_name(str : optional): Your last name if not provided nothing
                                      will be printed only first name.

    Return:
        There is a comment return line you can uncomment that if you want
        the string to be returned for test or other reasons.
        if not nothing is returned.
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    formated = "My name is {} {}".format(first_name, last_name)
    print(formated)
    # if you want to get the format value returned uncomment the line below.
    # return (formated)
