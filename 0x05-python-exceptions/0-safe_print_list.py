#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    index = 0
    for index in range(x):
        try:
            print(my_list[index], end='')
        except IndexError:
            print()
            return index
    print()
    return index + 1
