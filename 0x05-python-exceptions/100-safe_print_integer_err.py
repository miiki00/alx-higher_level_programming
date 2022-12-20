#!/usr/bin/python3
from sys import stderr


def safe_print_integer_err(value):
    try:
        "{:d}".format(value)
    except Exception as err:
        stderr.write("Exception: {}".format(err))
        return (False)
    else:
        print("{:d}".format(value))
        return (True)
