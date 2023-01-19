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

    def to_json(self, attrs=None):
        """to_json: method.
        This methods returns the dictinary description of
        a Student object.

        Args:
            attrs(list: optional): list of attributes to bet returned
                                   in the dictionary description.

        Return:
            The dictinary description of a Student object.
        """
        if attrs is None:
            return (self.__dict__)
        originalDict = self.__dict__
        filteredAttrs = []
        for attr in attrs:
            if attr in originalDict.keys():
                filteredAttrs.append(attr)
        customDict = dict.fromkeys(filteredAttrs)
        for attr in filteredAttrs:
            customDict[attr] = originalDict[attr]
        return (customDict)

    def reload_from_json(self, json):
        """reload_from_json: method
        Reloads a Student object from a dictionary description.

        Args:
            json(dict): Deserialized json dictionary description
                        of a Student object to reload from.
        Return:
            None.
        """

        jsonKeys = json.keys()

        if 'first_name' in jsonKeys:
            self.first_name = json['first_name']
        if 'last_name' in jsonKeys:
            self.last_name = json['last_name']
        if 'age' in jsonKeys:
            self.age = json['age']
