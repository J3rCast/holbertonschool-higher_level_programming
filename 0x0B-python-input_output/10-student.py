#!/usr/bin/python3
"""This module contains Student
that defines a student by:
"""


class Student:
    """This class defines a student"""
    def __init__(self, first_name, last_name, age):
        """Arguments:
            firs_name - first name of the student
            last_name - last name of the student
            age - age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
            retrieves a dictionary representation of a Student instance
        """
        new_dict = {}
        if attrs and type(attrs) is list:
            for i in attrs:
                if type(i) is not str:
                    return self.__dict__
                if hasattr(self, i):
                    new_dict[i] = getattr(self, i)
            return new_dict

        return self.__dict__
