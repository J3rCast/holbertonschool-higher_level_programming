#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None

    biggest_number = 0

    for i in my_list:
        if i > biggest_number:
            biggest_number = i

    return biggest_number
