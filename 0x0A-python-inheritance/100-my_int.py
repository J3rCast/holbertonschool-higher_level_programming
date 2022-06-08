#!/usr/bin/python3
"""This module contains a class
called MyInt
"""


class MyInt(int):
    """MyInt is a rebel. MyInt has == and
    != operators inverted
    """

    def __init__(self, integer):
        """This initialize the class"""
        self._MyInt__integer = integer

    def __eq__(self, other):
        """This method return a boolean"""
        return not type(self) == type(other)
