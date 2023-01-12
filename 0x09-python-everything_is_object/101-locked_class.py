#!/usr/bin/python3
"""
Contains a LockedClass that won't let users create attributes
dynamically.

Classes:
    LockedClass : As it's name suggest it's locked class.
"""


class LockedClass:
    """
    This is a locked class meaning users can't create attributes dynamically.
    """
    def __init__(self):
        """constructory"""
        pass

    def __setattr__(self, key, value):
        """
        manages how attributes are assigned.
        """
        if key != "first_name":
            raise AttributeError("'{}' object has no attribute "
                                 "'{}'".format(type(self).__name__, key))
