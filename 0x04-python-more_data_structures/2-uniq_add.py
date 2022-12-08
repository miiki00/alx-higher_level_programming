#!/usr/bin/python3

def uniq_add(my_list=[]):
    add = 0
    copyList = set(my_list)

    for i in copyList:
        add = add + i
    return (add)
