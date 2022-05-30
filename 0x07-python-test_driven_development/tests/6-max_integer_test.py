#!/usr/bin/python3
"""Unittest for max_integer([..])
"""


import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test the max integer funtcion."""
    def test_max0(self):
        """Firs test of max integer in a list of ints"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 4, 3, 2]), 4)

    def test_max1(self):
        """Firs test of max integer in a list of floats"""
        self.assertEqual(max_integer([1.4, 1.6, 1.9, 1.9]), 1.9)
        self.assertEqual(max_integer([1.9, 5.7, 1.8, 2]), 5.7)

    def test_max2(self):
        """Firs test of max integer in a string"""
        self.assertEqual(max_integer("Holberton"), 't')

    def test_max3(self):
        """Firs test of max integer in a empty list"""
        self.assertEqual(max_integer([]), None)

    def test_max4(self):
        """Firs test of max integer in a list of negative ints"""
        self.assertEqual(max_integer([-1, -3, -5, -7]), -1)

    def test_max5(self):
        """Firs test of max integer in a one elements list"""
        self.assertEqual(max_integer([7]), 7)


if __name__ == '__main__':
    unittest.main()
