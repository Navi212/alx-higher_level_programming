#!/usr/bin/python3
"""
The ``4-print_square`` module supplies a function that prints
a square with ``#`` character.
Here is the function ``print_square()

Example:

>>>print_square(5)
#####
#####
#####
#####
#####
"""


def print_square(size):
    """ Prints a square with ``#`` characterc. """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be an integer")
    if not isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        print("#" * size)


if __name__ == "__main__":
    print_square(10)
