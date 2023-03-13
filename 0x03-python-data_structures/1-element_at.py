#!/usr/bin/python3

def element_at(my_list, idx):
    """Retrives an element from a list"""
    list_len = len(my_list)
    if idx < 0:
        return None
    if idx > list_len:
        return None
    for i in my_list:
        val = my_list[idx]
        return val
