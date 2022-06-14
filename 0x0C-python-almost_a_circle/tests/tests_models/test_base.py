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

if __name__ == '__main__':
    unittest.main()
