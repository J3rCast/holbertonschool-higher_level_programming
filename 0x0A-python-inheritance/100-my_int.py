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
        self.__integer = integer

    def __eq__(self, other):
        """This method return a boolean"""
        if type(self) == type(other):
            return False
        if type(self) != type(other):
            return True
