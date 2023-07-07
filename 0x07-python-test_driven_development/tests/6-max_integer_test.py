#!/usr/bin/python3
# 6-max_integer_test.py
"""Unittests for the max_integer([..])."""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer([..])."""

    def test_ordered_list(self):
        """Test an ordered list of integers."""
        ordered = [3, 4, 5, 6]
        self.assertEqual(max_integer(ordered), 6)

    def test_unordered_list(self):
        """Test an unordered list of integers."""
        unordered = [4, 3, 6, 5]
        self.assertEqual(max_integer(unordered), 6)

    def test_max_at_begginning(self):
        """Test a list with a beginning max value."""
        max_at_beginning = [6, 5, 4, 3]
        self.assertEqual(max_integer(max_at_beginning), 6)

    def test_empty_list(self):
        """Test an empty list."""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_one_element_list(self):
        """Test a list with a single element."""
        one_element = [7]
        self.assertEqual(max_integer(one_element), 7)

    def test_floats(self):
        """Test a list of floats."""
        floats = [7.5, 10.3, 8.9, 13.5]
        self.assertEqual(max_integer(floats), 13.5)

    def test_ints_and_floats(self):
        """Test a list of ints and floats."""
        ints_and_floats = [7.5, 10.3, 6, 9]
        self.assertEqual(max_integer(ints_and_floats), 10.3)

    def test_string(self):
        """Test a string."""
        string = "Mary"
        self.assertEqual(max_integer(string), 'y')

    def test_list_of_strings(self):
        """Test a list of strings."""
        strings = ["Mary", "is", "my", "name"]
        self.assertEqual(max_integer(strings), "name")

    def test_empty_string(self):
        """Test an empty string."""
        self.assertEqual(max_integer(""), None)

if __name__ == '__main__':
    unittest.main()
