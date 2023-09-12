#!/usr/bin/python3
"""Student class module"""


class Student:
    """A class that defines a Student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Defines a method that retrieves a dictionary
        representation od a Student instance.
        """
        return self.__dict__
