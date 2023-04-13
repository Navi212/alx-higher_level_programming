#!/usr/bin/python3
import json


"""
The ``4-from_json_string`` module supplies a function
``from_json_string()`` that returns an objetc represented
by a JSON string.
"""


def from_json_string(my_str):
    """ Returns an object represented by a JSON string.

    Args:
        my_str - string representing a JSON string.

    Return:
        JSON object.
    """
    return(json.loads(my_str))
