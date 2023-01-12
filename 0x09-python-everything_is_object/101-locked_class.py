#!/usr/bin/python3
"""
Contains a LockedClass that won't let users create attributes
dynamically.

Classes:
    LockedClass : As it's name suggest it's locked class.
"""


class LockedClass:
    """
    Deomonestration of a locked class
    """

    def __setattr__(self, key, value):
        if key != "first_name":
            raise AttributeError("'{}' object has no attribute "
                                 "'{}'".format(type(self).__name__, key))
