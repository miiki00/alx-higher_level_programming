#!/usr/bin/python3
"""Module: base.py
This modules contains a class that define a Base for
other subclasses.

Classes:
    Base: Defines a base class for all subclasses under it.
"""


import json


class Base:

    """Class: Base
    Base : The base class for all subclasses under it.

    Attributes:
        id (int): A unique id of the object being created.

    This is a documentation for the constructor method.

    Args:
        id (int): A unique id of the object being created.
    """

    __nb_objects = 0

    def __init__(self, id=None):

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        """
        if list_dictionaries is not None:
            return (json.dumps(list_dictionaries))
        return ("[]")

    @staticmethod
    def from_json_string(json_string):
        """

        """
        if json_string is not None and len(json_string) != 0:
            return (json.loads(json_string))
        return ([])

    @classmethod
    def save_to_file(cls, list_objs):
        """
        save_to_file: saves list of objects into a file after changing
                      then to their dictionary json representation.
                      File name is going to be named after the objects
                      class.

        Args:
            list_objs: list of objects to save to the file.

        Return:
            None.
        """
        list_dict = []
        if list_objs is not None:
            for i in list_objs:
                list_dict.append(i.to_dictionary())
        else:
            list_dict = None

        json_rep = cls.to_json_string(list_dict)

        with open(f"{cls.__name__}.json", "w") as file:
            file.write(json_rep)

    @classmethod
    def load_from_file(cls):
        """
        load_from_file: loads json string and convert it to list of instances.

        Args:
            None.

        Return:
            the list of the loaded instances.
        """
        list_obj = []

        try:
            with open(f"{cls.__name__}.json", "r") as file:
                json_string = file.read()
            list_dict = cls.from_json_string(json_string)
            for i in list_dict:
                list_obj.append(cls.create(**i))
        except FileNotFoundError:
            pass
        return (list_obj)

    @classmethod
    def create(cls, **dictionary):
        """
        create: creates an object from a dictionary representation.

        Args:
            dictionary: the dictionary representation of the object.

        Return:
            The object created.
        """
        i = 1
        if cls.__name__ == "Square":
            i = 0
        obj = cls(1, i)
        obj.update(**dictionary)
        return (obj)
