#!/usr/bin/python3
"""This module contain a class
that inherits from list
"""


class MyList(list):
    """This class that inherits from list"""

    def print_sorted(self):
        """prints in ascending order"""
        
        print(sorted(self))
