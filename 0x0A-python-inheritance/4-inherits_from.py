#!/usr/bin/python3
"""This module has a function that
returns True if the object is an instance
of a class that inherited (directly or indirectly)
from the specified class ; otherwise False.
"""


def inherits_from(obj, a_class):
    """ Arguments:
            obj: object to check
            a_class: class specified

        Return:
            True if is instance, False otherwise
    """
    if isinstance(obj, a_class) and not type(obj) == a_class:
        return True
    return False
