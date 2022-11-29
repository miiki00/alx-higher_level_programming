#!/usr/bin/python3

def uppercase(str):
    last = ""
    for s in str:
        alp_var = ord(s)
        if alp_var >= 97 and alp_var <= 122:
            alp_var = alp_var - 32
            alp_var = chr(alp_var)
            last = last + alp_var
        else:
            last = last + s
    print("{}".format(last))
