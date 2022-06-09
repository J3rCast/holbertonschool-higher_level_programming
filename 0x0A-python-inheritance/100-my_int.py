#!/usr/bin/python3
"""This module contains a class
called MyInt
"""


class MyInt(int):
    """MyInt is a rebel. MyInt has == and
    != operators inverted
    """

    def __init__(self, value):
        """Initialize the class"""
        self.__value = value

    def __eq__(self, other):
        """This method return a boolean"""
        if self.__value == other:
            return False
        if self.__value != other:
            return True

    def __ne__(self, other):
        if self.__value != other:
            return False
        if self.__value == other:
            return True
