#!/usr/bin/python3

def element_at(my_list, idx):
    """Retrives an element from a list"""
    list_len = len(my_list)
    if (idx < 1 or idx > list_len -1):
        return None
    return my_list[idx]
