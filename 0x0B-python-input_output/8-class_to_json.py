#!/usr/bin/python3
"""The 8-class_to_json module supplies a function."""


import json


def class_to_json(obj):
    """ Returns dict. description for JSON object. """
    return obj.__dict__
