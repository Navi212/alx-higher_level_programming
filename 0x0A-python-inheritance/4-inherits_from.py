#!/usr/bin/python3
"""
The "4-inherits_from" supplies a function inherits_from()
that checks if an Object is instance of a class that inherited
(directly of indirectly) from a specified class.
"""


def inherits_from(obj, a_class):
    """ Returns True of obj is an instance of a_class.

    Args:
        obj - object.
        a_class - class.

    Return:
        True if true.
        False if false.
    """
    return (isinstance(obj, a_class) or issubclass(type(obj), a_class))
