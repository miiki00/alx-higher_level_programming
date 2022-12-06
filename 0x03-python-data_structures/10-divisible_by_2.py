#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    divList = []
    for i in my_list:
        divList.append(True if i % 2 == 0 else False)
    return (divList)
