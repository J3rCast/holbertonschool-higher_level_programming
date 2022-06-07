#!/usr/bin/python3
"""This module conains a class called BaseGeometry
"""


class BaseGeometry:
    """empty class"""
    def area(self):
        """This method defines the area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """This method validates value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
