#!/usr/bin/python3
"""
The 5-save_to_json_file module supplies a function save_to_json_file().
This function writes an object to a text file.
"""


import json


def save_to_json_file(my_obj, filename):
    """ Writes Object to a textfile.

    Args:
        my_obj - Object.
        filename - file.
    """
    with open(filename, "w") as file:
        return (json.dump(my_obj, file))
