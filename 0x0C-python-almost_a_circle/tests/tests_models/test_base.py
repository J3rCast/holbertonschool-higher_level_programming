#!/usr/bin/python3
"""This module is the unitest for base"""


import unittest
from unittest import TestCase
from unittest.mock import patch
from io import StringIO
from models.rectangle import Rectangle
from models.base import Base

class TestBaseMethods(unittest.TestCase):
    """Class to test Base methods"""
    @patch('builtins.print')
    def testIdPrint(self, mock_print):
        """Test if print id works"""
        b1 = Base()
        print(b1.id)
        mock_print.assert_called_with(1)
        b2 = Base()
        print(b2.id)
        mock_print.assert_called_with(2)

    def testToJsonString(self):
        """Test of toJsonString method."""
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        correct = "[{\"x\": 2, \"y\": 8, \"id\": 3, \"height\": 7, \"width\": 10}]\n"

        with patch('sys.stdout', new=StringIO()) as f:
            print(json_dictionary)
            self.assertEqual(f.getvalue(), correct)

        json_dictionary = Base.to_json_string([])
        correct = "[]\n"

        with patch('sys.stdout', new=StringIO()) as f:
            print(json_dictionary)
            self.assertEqual(f.getvalue(), correct)

if __name__ == '__main__':
    unittest.main()
