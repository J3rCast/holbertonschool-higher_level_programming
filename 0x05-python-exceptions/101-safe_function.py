#!/usr/bin/python3
import sys

def safe_function(fct, *args):
    result = 0
    try:
        result = fct(*args)
        return result
    except (ZeroDivisionError, TypeError, ValueError, IndexError) as x:
        sys.stderr.write("Exception: {}\n".format(x))
        return None
