#!/usr/bin/python3

# /*            start           */
# uppercase - prints a string in uppper case.
# str: The string to be printed in upper case.
#
# Return: void
# /*            finish          */
def uppercase(str):
    for i in range(len(str)):
        n = ord(str[i])
        check = n >= ord('a') and n <= ord('z')
        print("{:s}".format(chr(n - 32) if check else str[i]), end="")
    print()
