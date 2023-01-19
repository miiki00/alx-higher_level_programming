#!/usr/bin/python3
"""
This module contains a class that defines a student
object.

Classes:
    Student:
        defines a student object.
"""


class Student:
    """Student: class
    This class defines a student object.

    Attributes:
        first_name (str): first name of the student.
        last_name (str): last name of the student.
        age (int): age of the student.

    This is a documentation for the constructor method.

    Args:
        first_name (str): first name of the student.
        last_name (str): last name of the student.
        age (int): age of the student
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """to_json: method.
        This methods returns the dictinary description of
        a Student object.

        Args:
            No Arguments.

        Return:
            The dictinary description of a Student object.
        """
        return (self.__dict__)
