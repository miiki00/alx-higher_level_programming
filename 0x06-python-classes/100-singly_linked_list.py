#!/usr/bin/python3


""" 100-singly_linked_list : Module

Contains a classes to define a singly linked list
implementation in python

Classes:
    Node : Node of a singly linked list.
    SinglyLinkedList : Defines a singly liked list  of Node objects.
"""


class Node:

    """ Node : Class
    A Class to that contains attributes and methods for a Node
    of a singly linked list.

    This is a descritption for the __init__ method of the class
    Args:
        data (int): The data to strore on the node.
        next_node (:obj: 'Node', optional) : The next Node object of the list.

    Attributes:
        data (int): The data stored on the node.
        next_node: The next Node object on the list
    """

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ data

        A getter property for the attribute data.
        Args:
            no Arguments.

        Return:
            The value of the __data attribute.
        """

        return (self.__data)

    @data.setter
    def data(self, value):
        """ data

        A setter property for the attribute __data.
        Args:
            value (int): The value to set to the attribute __data.

        Return:
            None
        """

        if type(value) is int:
            self.__data = value
        else:
            raise TypeError("data must be and integer")

    @property
    def next_node(self):
        """ next_node

        A getter property for the attribute next_node
        Args:
            no Arguments.

        Return:
            The value of the attribute __next_node.
        """

        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """ data

        A setter property for the attribute __next_node.
        Args:
            value (:obj: 'Node'): The value to set to the
            attribute __next_node.

        Return:
            None
        """

        if type(value) is Node or value is None:
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """ SinglyLinkedList : Class

    A class That defines a singly linked list

    This is a discription for the class method __init__.
    Args:
        no Arguments:

    Attributtes:
        sorted_insert : method to insert a Node in to a sorted list.
    """

    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        """ sorted_insert

        Performes a sorted insert on an object type of SinglyLinkedList
        Args:
            value (int): The value of the node that is going to inserted

        Return:
            None
        """

        new_node = Node(value)
        old_node = self.__head
        before_old = None

        if self.__head is not None:
            while old_node.data < value and old_node.next_node is not None:
                before_old = old_node
                old_node = old_node.next_node
        if self.__head is None:
            new_node.next_node = old_node
            self.__head = new_node
        elif old_node == self.__head and old_node.data >= value:
            new_node.next_node = old_node
            self.__head = new_node
        elif old_node.data >= value:
            new_node.next_node = old_node
            before_old.next_node = new_node
        else:
            old_node.next_node = new_node

    def __str__(self):
        """ __str__
        Presents the list to be printed correctly to stdout.
        Args:
            no Arguments

        Return:
            The format string of the list elements.
        """

        to_print = ''
        nodes = self.__head

        while nodes is not None:
            if nodes.next_node is not None:
                to_print += "{}\n".format(nodes.data)
            else:
                to_print += "{}".format(nodes.data)
            nodes = nodes.next_node
        return (to_print)
