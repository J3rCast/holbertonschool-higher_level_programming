#!/usr/bin/python3
"""This module contains a function
that prints a <first name> and
prints <last name>
"""


def say_my_name(first_name, last_name=""):
    """Arguments:
        first_name: string that contains
            the first name
        last_name: string that contains
            the last name

       Returns:
        Errors: if <first_name> or <last_name>
            are not strings
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
