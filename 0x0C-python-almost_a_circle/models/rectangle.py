#!/usr/bin/python3
"""
The rectangle module is a subclass of the Base class.
"""


from models.base import Base


class Rectangle(Base):
    """ Rectangle a subclass of Base  defines a class. """
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ Gets the width. """
        return (self.__width)

    @width.setter
    def width(self, value):
        """ Sets the width property. """
        self.validate_attr("width", value)
        self.__width = value

    @property
    def height(self):
        """ Gets the height. """
        return (self.__height)

    @height.setter
    def height(self, value):
        """ Sets the height property. """
        self.validate_attr("height", value)
        self.__height = value

    @property
    def x(self):
        """ Gets the x value. """
        return (self.__x)

    @x.setter
    def x(self, value):
        """ Sets the x property. """
        self.validate_attr("x", value)
        self.__x = value

    @property
    def y(self):
        """ Gets the y value. """
        return (self.__y)

    @y.setter
    def y(self, value):
        """ Sets the y property. """
        self.validate_attr("y", value)
        self.__y = value

    def area(self):
        """ Defines the area of a rectangle. """
        return (self.width * self.height)

    def display(self):
        """ Prints Rectangle instance with # char to stdout. """
        for y in range(self.y):
            print("")
        for h in range(self.height):
            for x in range(self.x):
                print(" ", end="")
            for w in range(self.width):
                print("#", end="")
            print("")

    def __str__(self):
        """ Prints a fine print. """
        return ("[Rectangle] ({}) {}/{} - {}/{}"
                .format(self.id, self.x, self.y, self.width, self.height))

    @staticmethod
    def validate_attr(attr, value):
        """ Validates attributes and values. """
        if (type(value) != int):
            raise TypeError("{} must be an integer".format(attr))
        elif (attr == "width" or attr == "height"):
            if (value <= 0):
                raise ValueError("{} must be > 0".format(attr))
        elif (attr == "x" or attr == "y"):
            if (value < 0):
                raise ValueError("{} must be >= 0".format(attr))
