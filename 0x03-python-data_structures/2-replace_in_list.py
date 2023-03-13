#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """Replaces an element of a list at a specified location"""

    list_len = len(my_list)
    if idx < 0:
        return my_list
    if idx > list_len:
        return my_list
    for i in my_list:
        my_list[idx] = element
        return my_list

