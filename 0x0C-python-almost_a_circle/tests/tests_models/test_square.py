#!/usr/bin/python3
"""This module is the unitest for Square"""


import unittest
from unittest import TestCase
from unittest.mock import patch
from io import StringIO
from models.square import Square
from models.base import Base

class TestSquareMethods(unittest.TestCase):
    def testErrorTypeStrings(self):
        """test when some element is a string """
        with self.assertRaises(TypeError):
            r2 = Square(10, "2")
        with self.assertRaises(TypeError):
            r3 = Square("1", 2)
        with self.assertRaises(TypeError):
            r4 = Square(10, 2, "10")

    def testErrorTypeFloat(self):
        """test when some element is a float """
        with self.assertRaises(TypeError):
            r2 = Square(10.3, 4)
        with self.assertRaises(TypeError):
            r3 = Square(10 , 4.1)
        with self.assertRaises(TypeError):
            r4 = Square(10, 4, 3.1)
        with self.assertRaises(TypeError):
            r5 = Square(10, 2.1, 3)

    def testErrorValue(self):
        """test when some element is negative """
        with self.assertRaises(ValueError):
            r2 = Square(-10, 2)
        with self.assertRaises(ValueError):
            r3 = Square(10, -2)
        with self.assertRaises(ValueError):
            r4 = Square(10, 2, -2)

    def testErrorZero(self):
        """ test if dimensions is zero """
        with self.assertRaises(ValueError):
            r2 = Square(0, 2)

    def testAreaMethod(self):
        """Test the area method"""
        r1 = Square(2, 2)
        self.assertEqual(r1.area(), 4)
        r2 = Square(5, 5)
        self.assertEqual(r2.area(), 25)

    def testStrMethod(self):
        """Test the str magic method"""
        s1 = Square(5)
        corret = "[Square] (14) 0/0 - 5\n"
        with patch('sys.stdout', new=StringIO()) as f:
            print(s1)
            self.assertEqual(f.getvalue(), corret)
        s2 = Square(2, 2)
        corret = "[Square] (15) 2/0 - 2\n"
        with patch('sys.stdout', new=StringIO()) as f:
            print(s2)
            self.assertEqual(f.getvalue(), corret)
