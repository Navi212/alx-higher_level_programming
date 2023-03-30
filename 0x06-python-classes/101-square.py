#!/usr/bin/python3
""" Square Module """


class Square:
    """ Defines a class Square. """
    def __init__(self, size=0, position=(0, 0)):
        """ Initializes the class Square.

        Args:
            size - size.
            position - positon with 2 cordinates.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """ Retrieves the position. """
        return (self.__positon)

    @position.setter
    def position(self, value):
        """ Sets the position. """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ Returns current square area. """
        return (self.__size * self.__size)

    def my_print(self):
        """ Prints the square with the character # to stdout. """
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")

    def __str__(self):
        """ Defines the print() representation of a Square. """
        if self.__size != 0:
            [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            if i != self.__size - 1:
                print("")
        return ("")
