#!/usr/bin/python3
""" Square Module """


class Square:
    """ Defines a class Square. """
    def __init__(self, size=0):
        """ Initializes the class Square.

        Args:
            size - size
        """
        self.size = size

    @property
    def size(self):
        """ Retrieves the size value. """
        return (self.__size)

    @size.setter
    def size(self, value):
        """ Sets the size value. """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Returns current square area. """
        return (self.__size * self.__size)
