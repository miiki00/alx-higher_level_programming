#!/usr/bin/python3
""" 3-matrix_divided : module
This module contains function that makes a scalar
division of matrix.
functions:
    matrix_divided(matrix, div):
        a function tha makes a scalar division of matrix.
    matrix_check_input(matrix, div):
        check the inputs passec to matrix if the are valid or not.
    matrix_exception_msg(code):
        internal function to manage matrix_divided error
"""


def matrix_divided(matrix, div):
    """ matrix_divided : function
    This function does a scalar division of a matrix.

    Args:
        matrix (int): The matrix (list of lists) to divide.
        div (int): The number to divide it with.

    Return:
        matrix with  same dimensions as the input but
        with results.
    """
    idx, length, returnList = 0, 0, []

    matrix_check_input(matrix, div)
    if len(matrix) != 0:
        length = len(matrix[0])
    for i in matrix:
        if type(i) is not list:
            matrix_exception_msg(1)
        if len(i) != length:
            matrix_exception_msg(2)
        returnList.append([])
        for j in i:
            if type(j) not in [int, float]:
                matrix_exception_msg(1)
            result = j / div
            result = float("{:0.2f}".format(result))
            returnList[idx].append(result)
        idx += 1
    return (returnList)


def matrix_check_input(matrix, div):
    """ matrix_check_input : function
    This function checks if a valid input is passed to the matrix_divide
    function.

    Args:
        matrix (list): the matrix argument passed to matrix_divided.
        div (int/float): The div argument passed to matrix_diviede.

    Return:
        if returned to the caller arguments are valid else
        inputs are invalid.
    """
    if type(div) not in [int, float]:
        matrix_exception_msg(0)
    elif div == 0:
        matrix_exception_msg(3)
    if type(matrix) is not list:
        matrix_exception_msg(1)
    if len(matrix) != 0:
        if type(matrix[0]) is not list:
            matrix_exception_msg(1)


def matrix_exception_msg(code):
    """ matrix_exception_msg : function.
    This function print the corresponding message to the passed error code.

    Args:
        code (int): The error code.

    Return:
        does not return.
    """
    message = ["div must be a number",
               "matrix must be a matrix (list of lists) of integers/floats",
               "Each row of the matrix must have the same size",
               "division by zero"]
    if code < 3:
        raise TypeError(message[code])
    else:
        raise ZeroDivisionError(message[code])
