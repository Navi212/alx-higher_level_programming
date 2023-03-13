#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    """Finds all multiples of 2 in a list"""

    new_list = my_list[:]
    for i in my_list:
        if i % 2 == 0:
            new_list[i] = True
        elif i % 2 != 0:
            new_list[i] = False
    return new_list
