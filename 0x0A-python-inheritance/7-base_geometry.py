#!/usr/bin/python3
"""
The "7-base_geometry" defines a class BaseGeometry.
"""


class BaseGeometry:
    """ Defines a class BaseGeometry """
    def area(self):
        """ Defines area. """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Defines a function that validates value. """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
