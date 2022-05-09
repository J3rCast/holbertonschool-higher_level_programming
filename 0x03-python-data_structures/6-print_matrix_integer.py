#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == [[]] or matrix is None:
        print()
    else:
        for i in range(len(matrix)):
            for idx in range(len(matrix[i])-1):
                print(f"{matrix[i][idx]} ", end='')
            print(f"{matrix[i][idx+1]}")
