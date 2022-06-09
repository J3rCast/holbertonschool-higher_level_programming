#!/usr/bin/python3
"""This module contains a function
that adds a new attribute to an object if
 its possible
 """

def add_attribute(obj, name, value):
    """This function adds a new attribute"""
    if hasattr(obj, name) is False:
        raise TypeError("can't add new attribute")

    setattr(obj, name, value)
