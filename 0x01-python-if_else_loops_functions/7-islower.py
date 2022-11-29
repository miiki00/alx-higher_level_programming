#!/usr/bin/python3

# islower - function that checks if a char is lower case or not
# @c: The character to check.
# Return: True if lower case, False if not.
def islower(c):
    n = ord(c)
    if n >= ord('a') and n <= ord('z'):
        return True
    else:
        return False
