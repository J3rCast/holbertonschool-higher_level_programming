#!/usr/bin/python3
"""This Module contain a function
that prints a square using '#' as
character
"""


def print_square(size):
    """ Arguments:
            Size: the size of the square

        Returns:
            Error: is Size is not an integer
            Otherwise: prints a square
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise TypeError("size must be >= 0")

    for i in range(size):
        for idx in range(size):
            print("#", end="")
        print()
