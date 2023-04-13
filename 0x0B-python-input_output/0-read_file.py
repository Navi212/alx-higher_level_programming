#!/usr/bin/python3
"""
The ``0-read_file`` module supplies a function
read_file() that reads a file ``filename``.
"""


def read_file(filename=""):
    """ Reads a text file(UTF8) and prints it to stdout. """
    with open(filename, "r" encoding="utf-8") as file:
        file_cont = file.read()
        print(file_cont)
