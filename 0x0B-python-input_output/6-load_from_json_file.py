#!/usr/bin/python3
"""
The module ``6-load_from_json_file`` supplies a function.
The load_from_json_file() function creates an object froma JSON file.
"""


import json


def load_from_json_file(filename):
    """ Creates an object from a JSON file. """
    with open(filename, "r") as file:
        return (json.load(file))
