#!/usr/bin/python3
"""
Contains a LockedClass's defination that won't let users create attributes
dynamically.
"""


class LockedClass:
    """
    Deomonestration of a locked class
    which wont let users create attributes dynamically to instances
    of this LockedClass.
    """

    __slots__ = ["first_name"]
