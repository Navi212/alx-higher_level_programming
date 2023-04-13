#!/usr/bin/python3
import json


"""
The ``3-to_json_string`` module supplies a function
def to_json_string() that returns the JSON representation
of an object.
"""


def to_json_string(my_obj):
    """ Returns JSON representation of my_obj.

    Args:
        my_obj - The object.

    Return:
        JSON representation of my_obj.
    """
    return json.dumps(my_obj)
