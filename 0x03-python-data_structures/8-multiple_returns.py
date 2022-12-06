#!/usr/bin/pytohn3

def multiple_returns(sentence):
    if sentence is None:
        length = 0
    else:
        length = len(sentence)
    return ((length, None if length == 0 else sentence[0]))
