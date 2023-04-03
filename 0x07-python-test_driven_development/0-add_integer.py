#!/usr/bin/python3
"""
Thhis is the 0-add_integer modeule.
The 0-add_integer module supplies a function called, add_integer().
For example usage:

>>>0-add_integer(10, 12)
22
"""


def add_integer(a, b=98):
    """ Returns the sum of 2 numbers """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))


if __name__ == "__main__":
    sum = add_integer(10.5, 10.66)
    print(sum)
