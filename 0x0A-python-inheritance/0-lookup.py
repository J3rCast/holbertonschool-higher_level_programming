#!/usr/bin/pythn3
"""This module has a function that
return a list of attributes and methods
of and object
"""


def lookup(obj):
    """ Arguments:
            obj: object to list

        Return:
            list of objects and methods of obj
    """
    return dir(obj)
