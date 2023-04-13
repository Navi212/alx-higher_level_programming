#!/usr/bin/python3
"""
The ``1-write_file`` module supplies a function
write_file() that writes a string to a txt file.
"""


def write_file(filename="", text=""):
    """ Writes a string to a txt file(UTF8).

    Args:
        filename - The file to write into.

    Return:
        Number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as file:
        return (file.write(text))
