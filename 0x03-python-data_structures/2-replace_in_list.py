#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """Replaces an element of a list at a specified location"""
    if (idx < 0 and idx > len(my_list) - 1):
        return my_list
    my_list[idx] = element
    return my_list

