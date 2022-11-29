#!/usr/bin/python3

# uppercase - prints a string in uppper case.
# str: The string to be printed in upper case.
#
# Return: void
def uppercase(str):
    length = len(str)
    for i in range(length + 1):
        if i == length:
            n = 10
        else:
            n = ord(str[i])
        check = n >= ord('a') and n <= ord('z')
        print("{:s}".format(chr(n - 32) if check else chr(n)), end="")
