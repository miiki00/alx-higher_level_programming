#!/usr/bin/python3
"""
This module contains a class that is inherited from list and
provides a method that  print a list in a sorted manner with
out changing the orginal list.

Classes:
    MyList : This is a class that is inherited from list and
    provides a method that  print a list in a sorted manner with
    out changing the orginal list.

Functions:
    No functions.
"""


class MyList(list):
    """ MyList : Class.
    This a class that is inherited from the class list and
    provides a method that  print a list in a sorted manner with
    out changing the orginal list.
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
        swapped = True
        copyList = self.copy()
        length = len(copyList)

        while swapped:
            swapped = False
            i, j = 0, 1
            while j < length:
                if copyList[i] > copyList[j]:
                    tmp = copyList[i]
                    copyList[i] = copyList[j]
                    copyList[j] = tmp
                    swapped = True
                i += 1
                j += 1
        print(copyList)
        # if you want you can uncommnet the return statment.
        # return (copyList)
