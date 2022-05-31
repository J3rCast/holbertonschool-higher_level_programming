#!/usr/bin/python3
"""This module contains a function that
divides a matrix, dividing every
number o a list of lists by "div"
"""


def matrix_divided(matrix, div):
    """Arguments:
        matrix: list of list of integers
        div: the matrix must be dive by this

       Returns:
        matrix: a list of list of integers divided by div
        Error: raise an errors if something fails
    """
    result = 0
    new_list = []
    indiv_list = []
    if div == float('inf'):
        div = 1
    if type(matrix) is not list:
        raise TypeError("matrix must be a\
 matrix (list of lists) of integers/floats")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for i in range(len(matrix)):
        if type(matrix[i]) is not list:
            raise TypeError("matrix must be a\
 matrix (list of lists) of integers/floats")
        for idx in matrix[i]:
            if type(idx) is not int and type(idx) is not float:
                raise TypeError("matrix must be a\
 matrix (list of lists) of integers/floats")
            result = idx / div
            indiv_list.append(round(result, 2))
        if i > 0 and (len(matrix[i]) is not len(matrix[i - 1])):
            raise TypeError("Each row of the matrix must have the same size")
        new_list.append(indiv_list)
        indiv_list = []

    return new_list
