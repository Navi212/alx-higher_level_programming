#!/usr/bin/python3
# 5-rectangle.py
""" The module ``5-rectangle`` defines a rectangle. """


class Rectangle:
    """ Defines a rectangle. """
    def __init__(self, width=0, height=0):
        """ Our initializer.

        Args:
            width(int) : with default value 0
            height(int): with default value 0
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

    def area(self):
        """ Returns the area. """
        return (self.width * self.height)

    def perimeter(self):
        """ Returns the perimeter. """
        if self.width == 0 or self.height == 0:
            return (0)
        else:
            return (2 * (self.width + self.height))

    def __str__(self):
        """ Prints a printable rectangle with '#' character. """
        if self.width == 0 or self.height == 0:
            return ("")
        size = "#" * self.__width
        string = ""
        for i in range(self.__height):
            if i == self.__height - 1:
                string += size
            else:
                string += (size + "\n")
        return (string)

    def __repr__(self):
        """ Returns official string representation of method ."""
        return ("Rectangle({:d}, {:d})".format(self.__width, self.__height))

    def __del__(self):
        """ Deletes a class object. """
        print("Bye rectangle...")
