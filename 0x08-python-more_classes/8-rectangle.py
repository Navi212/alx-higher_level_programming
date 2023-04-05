#!/usr/bin/python3
# 8-rectangle.py
"""
The module ``8-rectangle`` defines a rectangle
and number of instances of the class.
"""


class Rectangle:
    """ Defines a rectangle.

    Attributes:
        number_of_instances(int) - class attribute.
        print_symbol(str) - class attribute
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Our initializer.

        Args:
            width(int) : with default value 0
            height(int): with default value 0
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        if self.__width == 0 or self.__height == 0:
            return ("")
        print_rec = []
        for i in range(self.__height):
            [print_rec.append(str(self.print_symbol)
                              ) for j in range(self.__width)]
            if i != self.__height - 1:
                print_rec.append("\n")
        return ("".join(print_rec))

    def __repr__(self):
        """ Returns official string representation of method ."""
        return ("Rectangle({:d}, {:d})".format(self.__width, self.__height))

    def __del__(self):
        """ Deletes a class object. """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
        return ("{}".format(Rectangle.number_of_instances))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ Returns the biggest rectangle based on the area.

        Attributes:
            rect_1 - rectangle 1
            rect_2 - rectange 2

        Return:
            The biggest rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() == rect_2.area() or rect_1.area() > rect_2.area():
            return (rect_1)
        return (rect_2)
