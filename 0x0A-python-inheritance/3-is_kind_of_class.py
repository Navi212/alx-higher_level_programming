#!/usr/bin/python3
"""
The "3-is_kind_of_class" module supplies a function is_kind_of_class
that checks if and Object is an instance of a Class.
"""


def is_kind_of_class(obj, a_class):
    """ Returns True if obj is instance of a_class

    Args:
        obj - object.
        a_class - class.

    Return:
        True if true.
        False if false.
    """
    if isinstance(obj, a_class):
        return (True)
    return (False)
