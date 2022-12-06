#!/usr/bin/python3

def max_integer(my_list=[]):
    length = len(my_list)

    if length == 0:
        return None
    for i in my_list:
        for j in my_list:
            if j > i:
                break
        if j == my_list[length - 1] and i >= j:
            return i
