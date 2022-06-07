#!/usr/bin/python3
"""This module has a function that
returns True if the object is exactly
an instance of the specified class ; otherwise False
"""


def is_same_class(obj, a_class):
    """ Arguments:
            obj: object to check
            a_class: class specified

        Return:
            True if is instance, False otherwise
    """
    if type(obj) == a_class:
        return True

    return False
