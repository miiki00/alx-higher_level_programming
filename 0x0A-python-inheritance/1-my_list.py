#!/usr/bin/python3
"""
This module contains a class that is inherited list and
provides a method that  print a list in a sorted manner with
out changing the orginal list.
Classes:
    MyList : This is a class that inherited list and
    provides a method that  print a list in a sorted manner with
    out changing the orginal list.
Functions:
    No functions.
"""


class MyList(list):
    """ MyList : Class.
    This a class that inherite the class list and
    provides a method that  print a list in a sorted manner with
    out changing the orginal list.
    It inherits list's constructor class so you can look more
    informationn of the on the documentation for the list class.
    """
    def print_sorted(self):
        """ print_sorted : method
        This method prints a MyList instance that contains a list of
        int objects in a sorted manner.
        Args:
            No Arguments.
        Return:
            You can uncomment the return statment if you need for any
            reasons I have used to test the function.
        """
        copyList = self.copy()
        copyList.sort()

        print(copyList)
        # if you want you can uncommnet the return statment.
        # return (copyList)
