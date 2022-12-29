#!/usr/bin/python3
"""
This module contains the functions that deal with formated printing.

Functions:
    text_indentation(text):
        prints text by splitting it with this '?', '.', ':' delimeters.
        when on of this delimeter is found 2 new lines are printed after
        it any white space is removed after it.
"""


def text_indentation(text):
    """ text_indentation : function.
    This function prints text by splitting it with this '?', '.', ':'
    delimeters. When on of this delimeter is found 2 new lines are printed
    after it any white space is removed after it.

    Args:
        text (str): The string to format

    Return:
        you can uncomment the return statment if you need it for any reason
        I added it for testing the function. but by default it does not
        return any thing.
    """
    toPrint = ""
    flag = False
    spaces = length = i = 0

    if type(text) is not str:
        raise TypeError("text must be a string")
    for j in reversed(text):
        if j in ' \t':
            spaces += 1
        else:
            break
    length = len(text) - spaces
    while i < length:
        if text[i] not in ' \t':
            flag = True
        if flag:
            toPrint += text[i]
        if text[i] in '?.:':
            toPrint += '\n\n'
            flag = False
        i += 1
    print(toPrint, end='')
    # if you want you can uncommnet the return statment.
    # return (toPrint)
