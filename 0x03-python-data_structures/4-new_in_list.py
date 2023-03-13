#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """
    Replaces an element in a list at a particular index without
    modifying the original list
    """

    list_len = len(my_list)
    list_copy = my_list[:]
    if idx < 0:
        return list_copy
    if idx > list_len:
        return list_copy
    for i in list_copy:
        list_copy[idx] = element
        return list_copy
