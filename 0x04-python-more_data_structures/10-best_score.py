#!/usr/bin/python3

def best_score(a_dictionary):
    dump = list(a_dictionary)
    length = len(dump)

    if length == 0:
        return None
    for i in dump:
        k = a_dictionary[i]
        for j in dump:
            j = a_dictionary[j]
            if j > k:
                break
        if j == a_dictionary[dump[length - 1]] and k >= j:
            return i
