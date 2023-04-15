#!/usr/bin/python3
"""
Tests our rectangle class.
"""


import unittest
from models.rectangle import Rectangle


class test_rectangle(unittest.TestCase):
    """ Tests rectangle class. """

    def test_rectangle_is_base(self):
        """ Tests if Rectangle is a subblass of Base. """
        self.assertIsInstance(Rectangle(10, 5), Base)

    def test_rectangle_no_arg(self):
        """ Tests a Rectangle with no args ."""
        with self.assertRaises(TypeError):
            Rectangle()

    def test_rectangle_one_arg(self):
        """ Tests a Rectange with 1 arg. """
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_two_args(self):
        r1 = Rectangle(1, 2)
        r2 = Rectangle(1, 3)
        self.assertEqual(r1.id, r2.id)

    def test_three_args(self):
        r1 = Rectangle(1, 2, 3)
        r2 = Rectangle(1, 3, 5)
        self.assertEqual(r1.id, r2.id)

    def test_four_args(self):
        r1 = Rectangle(1, 3, 5, 6)
        r2 = Rectangle(1, 3, 2, 7)
        self.assertEqual(r1.id, r2.id)

    def test_five_args(self):
        r1 = Rectangle(9, 2, 1, 3, 4)
        r2 = Rectangle(11, 2, 3, 5, 4)
        self.assertEqual(r1.id, r2.id)

    def test_more_args(Self):
        r1 = Rectangle(1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
        r2 = Rectangle(1, 2, 1, 2, 3, 4, 5, 6, 4, 1)
        self.assertEqual(r1.id, r2.id)

        def test_five_args(self):
        self.assertEqual(7, Rectangle(10, 2, 0, 0, 7).id)

    def test_more_than_five_args(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)

    def test_width_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__width)

    def test_height_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__height)

    def test_x_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__x)

    def test_y_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__y)

    def test_width_getter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(5, r.width)

    def test_width_setter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        r.width = 10
        self.assertEqual(10, r.width)

    def test_height_getter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(7, r.height)

    def test_height_setter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        r.height = 10
        self.assertEqual(10, r.height)

    def test_x_getter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(7, r.x)

    def test_x_setter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        r.x = 10
        self.assertEqual(10, r.x)

    def test_y_getter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(5, r.y)

    def test_y_setter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        r.y = 10
        self.assertEqual(10, r.y)
