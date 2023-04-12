#!/usr/bin/python3
"""
This is the "2-is_same_class" module.
The 2-is_same_class supplies a function, is_same_class()
which returns True if the object is exactly an instance
of the specified class ; otherwise False.
"""


def is_same_class(obj, a_class):
    """ Returns True if obj is exactly an instance of a_class.

    Args:
        obj - object to check.
        a_class - class to check with.

    Return:
        True if true.
        False if false.
    """
    if isinstance(obj, a_class):
        return True
    return False
