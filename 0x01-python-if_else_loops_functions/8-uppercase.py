#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        n = ord(str[i])
        check = n >= ord('a') and n <= ord('z')
        print("{:s}".format(chr(n - 32) if check else str[i]), end="")
    print("")
