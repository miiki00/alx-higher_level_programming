#!/usr/bin/python3
"""
contains definations of MyList.
"""


class MyList(list):
    """ Inherited from list"""

    def print_sorted(self):
        """ prints a list sorted"""
        copyList = sorted(self)
        print(copyList)
        # if you want you can uncommnet the return statment.
        # return (copyList)
