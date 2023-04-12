#!/usr/bin/python3
"""
The "8-rectangle" module inherits from class BaseGeometry.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Defines a class that inherits from BaseGeometry. """
    def __init__(self, width, height):
        """ Initialize a new Rectangle.

        Args:
            width(int) - The width of the new rectangle.
            height(int) - The height of the new rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ Returns the area of a rectangle. """
        return (self.__width * self.__height)

    def __str__(self):
        return ("[{}] {}/{}".format(type(self).__name__, self.__width, self.__height))
