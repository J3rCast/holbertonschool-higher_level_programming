#!/usr/bin/python3
"""
This module contains a function that adds two number
if some of the arguments is not an int of a float
raise a type error
"""


def add_integer(a, b=98):
    """Arguments:
        a: first number
        b: second number of 98

       Returns:
        int: sum of a and b
        Error: if something fails
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(a) is not float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)


if __name__ == "__main__":
    import doctest
    doctest.testmod("tests/0-add_integer.txt")
