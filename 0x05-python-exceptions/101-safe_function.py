#!/usr/bin/python3
from sys import stderr


def safe_function(fct, *args):
    try:
        return_value = fct(args[0], args[1])
    except Exception as err:
        stderr.write("Exception: {}\n".format(err))
        return (None)
    else:
        return (return_value)
