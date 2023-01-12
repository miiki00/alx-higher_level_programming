#!/usr/bin/python3
def magic_string():
    magic_string.cnt = getattr(magic_string, 'cnt', 0) + 1
    return ("Best School, " * (magic_string.cnt - 1) + "Best School")
