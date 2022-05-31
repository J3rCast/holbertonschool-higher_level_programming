#!/usr/bin/python3
"""This module contains a simple
class called Rectangle with some
properties defined
"""


class Rectangle:
    """This is a simple class"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
        self.__width = width
        Rectangle.number_of_instances += 1

    def area(self):
        """Return the area of the rectangle."""
        area_value = self.__height * self.__width
        return area_value

    def perimeter(self):
        """Return the perimeter of the rectangle"""
        if self.__height == 0 or self.__width == 0:
            perimeter_value = 0
        else:
            perimeter_value = (self.__height * 2) + (self.__width * 2)
        return perimeter_value

    def __str__(self):
        """This method is called when print() is used"""
        rect = ""
        if self.__height == 0 or self.__width == 0:
            return rect
        for heig in range(self.__height):
            for wid in range(self.__width):
                rect += "#"
            if heig < self.__height - 1:
                rect += "\n"
        return rect

    def __repr__(self):
        """This method is called when repr() is used"""
        represetation = "Rectangle(" + str(self.__width)\
            + ", " + str(self.__height) + ")"
        return represetation

    def __del__(self):
        """This method is used when a instance is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """getter of the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter of the width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter of the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter of the height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
