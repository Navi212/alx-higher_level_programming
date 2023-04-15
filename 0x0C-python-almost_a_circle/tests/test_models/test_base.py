#!/usr/bin/python3
"""
This is a module for conducting unittests.
"""


import unittest
from models.base import Base


class test_base(unittest.TestCase):
    """ Tests base class. """
    def test_id_none(self):
        """ Tests if id is None. """
        b = Base()
        self.assertEqual(1, b.id)

    def test_id_zero(self):
        """ Tests if id 0. """
        b = Base(0)
        self.assertEqual(0, b.id)

    def test_id_pos_num(self):
        """ Tests id for positive number. """
        b = Base(10)
        self.assertEqual(10, b.id)

    def test_id_neg_num(self):
        """ Tests id for negative number. """
        b = Base(-15)
        self.assertEqual(-15, b.id)

    def test_id_list(self):
        """ Tests id for non int. """
        b = Base([1, 2, 3, 4, 5])
        self.assertEqual([1, 2, 3, 4, 5], b.id)
        
    def test_id_str(self):
        """ Tests id for string. """
        b = Base("Jay")
        self.assertEqual("Jay", b.id)

    def test_id_dict(self):
        """ Tests id for non int. """
        b = Base({"name": "ken"})
        self.assertEqual({"name": "ken"}, b.id)

    def test_id_tup(self):
        """ Tests if for non int. """
        b = Base(("Joe", 99))
        self.assertEqual(("Joe", 99), b.id)
