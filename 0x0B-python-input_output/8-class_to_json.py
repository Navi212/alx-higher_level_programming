#!/usr/bin/python3
"""
The ``8-class_to_json`` module supplies a function.
The ``def class_to_json()`` function returns the dict-
ionary description for JSON serialization object.
"""


import json


def class_to_json(obj):
    """ Returns dict. description for JSON sterilation object. """
    return (obj.__dict__)
