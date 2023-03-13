#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    """Deletes the item at a specific position in a list"""

    list_len = len(my_list)
    if idx < 0:
        return my_list
    elif idx > list_len:
        return my_list
    else:
        for i in my_list:
            del my_list[idx]
            return my_list
