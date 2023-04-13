#!/usr/bin/python3

"""
The ``2-append_write`` module supplies a function
append_write() that appends a string at the end of
a text file(UTF8) and returns the number of characters.
"""


def append_write(filename="", text=""):
    """ Appends a string at the end of a text file(UTF8).

    Args:
        filename - file to append into.
        text - string to append into filename.

    Return:
        Number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as file:
        num_chars = file.write(text)
        return(num_chars)
