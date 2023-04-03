#!/usr/bin/python3
"""
The ``3-say_my_name`` module supplies a function that prints
first name and last name
Function name is ``say_my_name()

Example:
>>>say_my_name("John", "Smith")
My name is John Smith
"""


def say_my_name(first_name, last_name=""):
    """ Prints a name """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    if len(first_name) == 0 and len(last_name) == 0:
        raise TypeError("Invalid input")
    print("My name is {} {}".format(first_name, last_name))


if __name__ == "__main__":
    say_my_name("Ok", "")
