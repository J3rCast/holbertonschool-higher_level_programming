#!/usr/bin/python3
"""Create a class called square."""


class Square:
    """class Square that defines a square by: (based on 3-square.py)"""
    def __init__(self, size=0, position=(0, 0)):
        """Private instance attribute: size"""
        self.__size = size
        if type(self.__size) != int:
            print("size must be an integer", end="")
            raise TypeError
        elif self.__size < 0:
            print("size must be >= 0", end="")
            raise ValueError
        self.__position = position
        if self.__position[0] < 0 or self.__position[1] < 0 or\
                type(self.__position[0]) != int or\
                    type(self.__position[1]) != int or len(self.__position) != 2:
            print("position must be a tuple of 2 positive integers")
            raise TypeError

    def area(self):
        """return the area of the square"""
        return self.__size ** 2

    @property
    def size(self):
        """getter of the size"""
        return self.__size

    @size.setter
    def size(self, new_size):
        """setter of the size"""
        if type(new_size) != int:
            print("size must be an integer", end="")
            raise TypeError
        elif new_size < 0:
            print("size must be >= 0", end="")
            raise ValueError
        self.__size = new_size

    @property
    def position(self):
        """getter of the position"""
        return self.__position

    @position.setter
    def position(self, value):
        """setter of the position"""
        if value[0] < 0 or value[1] < 0 or type(value[0]) != int or\
                type(value[1]) != int or len(value) != 2:
            print("position must be a tuple of 2 positive integers", end="")
            raise TypeError
        self.__position = value

    def __str__(self):
        """print a square based on size"""
        square = ""
        rows = 0
        columns = 0
        if self.__size == 0:
            square = "\n"
        else:
            for i in range(self.__position[1]):
                square = square + "\n"
            while columns < self.__size:
                for i in range(self.__position[0]):
                    square = square + " "
                while rows < self.__size:
                    square = square + "#"
                    rows += 1
                if columns < self.__size - 1:
                    square = square + "\n"
                rows = 0
                columns += 1
        return square
