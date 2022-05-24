#!/usr/bin/python3
class Square:
    """class Square that defines a square by: (based on 3-square.py)"""
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

    def my_print(self):
        """print a square based on size"""
        rows = 0
        columns = 0
        if self.__size == 0:
            print()
        else:
            while columns < self.__size:
                while rows < self.__size:
                    print("#", end="")
                    rows += 1
                print()
                rows = 0
                columns += 1
