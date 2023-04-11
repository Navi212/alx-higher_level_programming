#!/usr/bin/python3
""" 0-lookup.py Module. """


def lookup(obj):
    """ returns the list of available attributes and methods of an object

    Args:
        obj - object argument.

    Return:
        List of available attributes and methods.
    """
    return (dir(obj))
