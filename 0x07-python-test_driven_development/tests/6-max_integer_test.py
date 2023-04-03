#!/usr/bin/python3
# 6-max_integer_test.py
"""
    Unittests for max_integer([...]).
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ Defines unittests for max_integer([...]). """

    def test_ord_li(self):
        """Test an ordered list of integers."""
        li = [1, 2, 3, 4]
        self.assertEqual(max_integer(li), 4)

    def test_unord_li(self):
        """Test an unordered list of integers."""
        li = [1, 2, 4, 3]
        self.assertEqual(max_integer(li), 4)

    def test_max_at_begginning(self):
        """Test a list with a beginning max value."""
        li = [4, 3, 2, 1]
        self.assertEqual(max_integer(li), 4)

    def test_empty_list(self):
        """Test an empty list."""
        li = []
        self.assertEqual(max_integer(li), None)

    def test_one_element_list(self):
        """Test a list with a single element."""
        li = [7]
        self.assertEqual(max_integer(li), 7)

    def test_floats(self):
        """Test a list of floats."""
        li = [1.53, 6.33, -9.123, 15.2, 6.0]
        self.assertEqual(max_integer(li), 15.2)

    def test_ints_and_floats(self):
        """Test a list of ints and floats."""
        li = [1.53, 15.5, -9, 15, 6]
        self.assertEqual(max_integer(li), 15.5)

    def test_empty_string(self):
        """Test an empty string."""
        self.assertEqual(max_integer(""), None)


if __name__ == "__main__":
    unittest.main()
