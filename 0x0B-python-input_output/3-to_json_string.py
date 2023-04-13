#!/usr/bin/python3
"""
The ``3-to_jason_string`` module supplies
a function to_json_string() which returns
the json representtation on an object.
"""


import json


def to_json_string(my_obj):
    """ json representation of an object.

    Args:
        my_obj - The object.

    Return:
        json object.
    """
    return (json.dumps(my_obj))
