#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    newDictionary = {}

    for i in list(a_dictionary):
        newDictionary[i] = a_dictionary[i] * 2
    return (newDictionary)
