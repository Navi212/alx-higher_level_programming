#!/usr/bin/python3
"""
The "8-rectangle" inherits from class BaseGeometry.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectange(BaseGeometry):
    """ Defines a class that inherits from BaseGeometry. """
    def __init__(self, width, height):
        """ Initialize a new Rectangle.

        Args:
            width(int) - The width of the new rectangle.
            height(int) - The height of the new rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
