#!/usr/bin/python3
"""This module is the unitest for rectangle"""


import unittest
from unittest import TestCase
from unittest.mock import patch
from io import StringIO
from models.rectangle import Rectangle
from models.base import Base

class TestRectangleMethods(unittest.TestCase):
    def testErrorTypeStrings(self):
        """test when some element is a string """
        with self.assertRaises(TypeError):
            r2 = Rectangle(10, "2")
        with self.assertRaises(TypeError):
            r3 = Rectangle("1", 2)
        with self.assertRaises(TypeError):
            r4 = Rectangle(10, 2, "10", 5)
        with self.assertRaises(TypeError):
            r5 = Rectangle(10, 2, 3, "4")

    def testErrorTypeFloat(self):
        """test when some element is a float """
        with self.assertRaises(TypeError):
            r2 = Rectangle(10.3, 4)
        with self.assertRaises(TypeError):
            r3 = Rectangle(10 , 4.1)
        with self.assertRaises(TypeError):
            r4 = Rectangle(10, 4, 3.1)
        with self.assertRaises(TypeError):
            r5 = Rectangle(10, 4, 3, 2.1)

    def testErrorValue(self):
        """test when some element is negative """
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

    def testAreaMethod(self):
        """Test the area method"""
        r1 = Rectangle(2, 2)
        self.assertEqual(r1.area(), 4)
        r2 = Rectangle(5, 5)
        self.assertEqual(r2.area(), 25)

    def testStrMethod(self):
        """Test the str magic method"""
        r1 = Rectangle(4, 6, 2, 1, 12)
        corret = "[Rectangle] (12) 2/1 - 4/6\n"
        with patch('sys.stdout', new=StringIO()) as f:
            print(r1)
            self.assertEqual(f.getvalue(), corret)
        r2 = Rectangle(4, 6)
        corret = "[Rectangle] (7) 0/0 - 4/6\n"
        with patch('sys.stdout', new=StringIO()) as f:
            print(r2)
            self.assertEqual(f.getvalue(), corret)

    def testDisplayMethod(self):
        """Test the Display method."""
        r1 = Rectangle(5, 5)
        with open('correct_DP.txt', mode="r") as f:
            corret = f.read()

        with patch('sys.stdout', new=StringIO()) as f:
            r1.display()
            self.assertEqual(f.getvalue(), corret)

    def testDisplayAxis(self):
        """Test the display method with axis."""
        r1 = Rectangle(5, 5, 2, 3)
        with open('correct_DP_axis.txt', mode="r") as f:
            corret = f.read()

        with patch('sys.stdout', new=StringIO()) as f:
            r1.display()
            self.assertEqual(f.getvalue(), corret)

    def testUpdateMethod(self):
        """Test the update method."""
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89)
        correct = "[Rectangle] (89) 10/10 - 10/10\n"

        with patch('sys.stdout', new=StringIO()) as f:
            print(r1)
            self.assertEqual(f.getvalue(), correct)

        r2 = Rectangle(10, 10, 10, 10)
        r2.update(89, 2)
        correct = "[Rectangle] (89) 10/10 - 2/10\n"

        with patch('sys.stdout', new=StringIO()) as f:
            print(r2)
            self.assertEqual(f.getvalue(), correct)

    def testUpdateKwargsMethod(self):
        """Test the update with kwargs method."""
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(height=89)
        correct = "[Rectangle] (8) 10/10 - 10/89\n"

        with patch('sys.stdout', new=StringIO()) as f:
            print(r1)
            self.assertEqual(f.getvalue(), correct)

        r2 = Rectangle(10, 10, 10, 10)
        r2.update(height=89,x=2, id=89)
        correct = "[Rectangle] (89) 2/10 - 10/89\n"

        with patch('sys.stdout', new=StringIO()) as f:
            print(r2)
            self.assertEqual(f.getvalue(), correct)


if __name__ == '__main__':
    unittest.main()
