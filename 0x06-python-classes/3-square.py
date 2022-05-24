#!/usr/bin/python3
"""Create a class called square."""


class Square:
    """class Square that defines a square by: (based on 2-square.py)"""
    def __init__(self, size=0):
        """Private instance attribute: size"""
        self.__size = size
        if type(self.__size) != int:
            print("size must be an integer", end="")
            raise TypeError
        elif self.__size < 0:
            print("size must be >= 0", end="")
            raise ValueError

    def area(self):
        """return the area of the square"""
        return self.__size ** 2
