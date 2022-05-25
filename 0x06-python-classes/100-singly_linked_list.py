#!/usr/bin/python3
"""create a linked list using classes"""


class Node:
    """create a node"""
    def __init__(self, data, next_node=None):
        self._data = data
        self._next_node = next_node

    @property
    def data(self):
        """getter of the data"""
        return self._data

    @data.setter
    def data(self, value):
        """setter of the data"""
        if type(value) != int:
            raise TypeError("data must be an integer")
        self._data = value

    @property
    def next_node(self):
        """getter of the data"""
        return self._next_node

    @next_node.setter
    def next_node(self, value):
        """setter of the next_node"""
        if value is not None or value is not Node():
            raise TypeError("next_node must be a Node object")
        self._next_node = value


class SinglyLinkedList:
    """create a new linked list"""
    def __init__(self):
        """create a linked list"""
        self.__head = None

    def sorted_insert(self, value):
        """insert a new node"""
        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node
        elif value < self.__head._data:
            new_node._next_node = self.__head
            self.__head = new_node
        else:
            temp = self.__head
            while temp._next_node and temp._next_node._data < value:
                temp = temp._next_node
            new_node._next_node = temp._next_node
            temp._next_node = new_node

    def __str__(self):
        """make the list printable"""
        temp = self.__head
        linked_list = ""
        while temp:
            if temp.next_node is None:
                linked_list += str(temp._data)
            else:
                linked_list += str(temp._data) + "\n"
            temp = temp._next_node

        return linked_list
