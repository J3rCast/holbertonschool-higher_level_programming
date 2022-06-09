#!/usr/bin/python3
"""This module contains a class
called MyInt
"""


class MyInt(int):
    """MyInt is a rebel. MyInt has == and
    != operators inverted
    """

    def __eq__(self, other):
        """This method return a boolean"""
        return False

    def __ne__(self, other):
        return True
