#!/usr/bin/python3
import json


def to_json_string(my_obj):
    """ Returns JSON representation of my_obj.

    Args:
        my_obj - The object.

    Return:
        JSON representation of my_obj.
    """
    return (json.dumps(my_obj))
