#!/usr/bin/python3
# 101-locked_class.py
"""Defines a Locked class. """


class LockedClass:
    """ Prevents the users from dynamically creating new instance attibutes.
        except the new instance attribute is callef first_name
    """
    __slots__ = ["first_name"]
