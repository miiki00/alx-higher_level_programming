#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    newList = my_list.copy()
    if idx >= 0 and idx < len(my_list):
        newList[idx] = element
    return (newList)
