#!/usr/bin/python3
# 1-rectangle.py
""" The module ``1-rectangle`` defines a rectangle. """


class Rectangle:
    """ Defines a rectangle. """
    def __init__(self, width=0, height=0):
        """ Initializer.

        Attributes:
            width(int) - width with default value 0
            height(int) - height with default value 0
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Returns the width. """
        return (self.__width)

    @width.setter
    def width(self, value):
        """ Sets the width. """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Returns the height. """
        return (self.__height)

    @height.setter
    def height(self, value):
        """ Sets the height. """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
