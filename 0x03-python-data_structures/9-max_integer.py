#!/usr/bin/python3

def max_integer(my_list=[]):
    """Finds the biggest integer of a list"""

    list_len = len(my_list)
    if list_len <= 0:
        return None
    max_val = my_list[0]
    for i in my_list:
        if my_list[i] > max_val:
            max_val = my_list[i]
        return max_val
