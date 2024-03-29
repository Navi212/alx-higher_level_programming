#!/usr/bin/python3
""" Square Module """


class Square:
    """ Defines a class Square. """
    def __init__(self, size=0):
        """ Initializes the class Square.

        Args:
            size - size
        """
        self.__size = size
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        if (self.__size < 0):
            raise ValueError("size must be >= 0")
