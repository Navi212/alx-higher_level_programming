#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):

    """Prints all integers in reverse order"""
    list_len = len(my_list)
    for i in reversed(my_list):
        print(i)
