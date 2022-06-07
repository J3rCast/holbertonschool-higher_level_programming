#!/usr/bin/pythn3
"""This module has a function that
returns True if the object is an instance of,
or if the object is an instance of a class that inherited from,
the specified class ; otherwise False
"""


def is_kind_of_class(obj, a_class):
    """ Arguments:
            obj: object to check
            a_class: class specified

        Return:
            True if is instance, False otherwise
    """
    return isinstance(obj, a_class)
