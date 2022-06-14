#!/usr/bin/python3
"""This module is the unitest for base"""


import unittest
from unittest import TestCase
from unittest.mock import patch
from io import StringIO
from models.rectangle import Rectangle
from models.base import Base

class TestRectangleMethods(unittest.TestCase):
    def testErrorTypeStrings(self):
        """ test if some element is a string """
        with self.assertRaises(TypeError):
            r2 = Rectangle(10, "2")
        with self.assertRaises(TypeError):
            r3 = Rectangle("1", 2)
        with self.assertRaises(TypeError):
            r4 = Rectangle(10, 2, "10", 5)
        with self.assertRaises(TypeError):
            r5 = Rectangle(10, 2, 3, "4")

    def testErrorTypeFloat(self):
        """ test if some element is a float """
        with self.assertRaises(TypeError):
            r2 = Rectangle(10.3, 4)
        with self.assertRaises(TypeError):
            r3 = Rectangle(10 , 4.1)
        with self.assertRaises(TypeError):
            r4 = Rectangle(10, 4, 3.1)
        with self.assertRaises(TypeError):
            r5 = Rectangle(10, 4, 3, 2.1)

    def testErrorValue(self):
        """ test if some element is negative """
        with self.assertRaises(ValueError):
            r2 = Rectangle(-10, 2)
        with self.assertRaises(ValueError):
            r3 = Rectangle(10, -2)
        with self.assertRaises(ValueError):
            r4 = Rectangle(10, 2, -2, 3)
        with self.assertRaises(ValueError):
            r5 = Rectangle(10, 2, 3, -4)

    def testErrorZero(self):
        """ test if dimensions is zero """
        with self.assertRaises(ValueError):
            r2 = Rectangle(0, 2)
        with self.assertRaises(ValueError):
            r3 = Rectangle(10, 0)
