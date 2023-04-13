#!/usr/bin/python3
"""
module for json string.
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
