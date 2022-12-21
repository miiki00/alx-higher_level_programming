#!/usr/bin/python3


upper = 89
lower = 122
while upper > 64:
    print("{}{}".format(chr(lower), chr(upper)), end='')
    upper -= 2
    lower -= 2
