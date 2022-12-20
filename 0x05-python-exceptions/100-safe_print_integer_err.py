#!/usr/bin/python3
from sys import stderr


def safe_print_integer_err(value):
    try:
        "{:d}".format(value)
    except BaseException as err:
        stderr.write("Exception: {}\n".format(err))
        return (False)
    else:
        print("{:d}".format(value))
        return (True)
