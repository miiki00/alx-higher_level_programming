#!/usr/bin/python3

def search_replace(my_list, search, replace):
    newList = []
    for x in my_list:
        if x == search:
            x = replace
        newList.append(x)
    return (newList)
