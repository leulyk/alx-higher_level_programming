#!/usr/bin/python3
"""
    Unittest for max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ Unit tests 6-max_integer.py """
    def test_max_integer_empty(self):
        """ test for empty list """
        self.assertEqual(max_integer([]), None)

    def test_max_integer_single_element(self):
        """ test for single element """
        self.assertEqual(max_integer([-6]), -6)

    def test_max_integer_positives(self):
        """ test for positive integers only """
        self.assertEqual(max_integer([1, 3, 2]), 3)

    def test_max_integer_negatives(self):
        """ add negative integers """
        self.assertEqual(max_integer([-3, -5, -1]), -1)

    def test_max_integer_floats(self):
        """ test for floating point numbers """
        self.assertEqual(max_integer([-3.8, -2.9, -5.8]), -2.9)

    def test_max_integer_mixed(self):
        """ mix integers and floats """
        self.assertEqual(max_integer([3, -2.3, 8.3, 5]), 8.3)

    def test_max_integer_tuple(self):
        """ test tuple """
        self.assertEqual(max_integer((2, -3, 4.5, 6)), 6)

    def test_max_integer_string(self):
        """ test string """
        self.assertEqual(max_integer("Software"), "w")

    def test_max_integer_int(self):
        """ pass integer as argument """
        with self.assertRaises(TypeError):
            max_integer(2)

    def test_max_integer_float(self):
        """ pass float as argument """
        with self.assertRaises(TypeError):
            max_integer(4.5)

    def test_max_integer_mixedtypes(self):
        """ test with mixed types in a list """
        with self.assertRaises(TypeError):
            max_integer([1, 2.3, 'hello'])

    def test_max_integer_dict(self):
        """ pass a dictionary as argument """
        with self.assertRaises(KeyError):
            max_integer({'a': 1, 'b': 2, 'c': 3})
