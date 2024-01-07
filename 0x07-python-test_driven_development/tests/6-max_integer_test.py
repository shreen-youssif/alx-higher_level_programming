#!/usr/bin/python3
"""Unitest for max_integer function"""
import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_regular_list(self):
        """test a regular list of integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_reverse_sorted_list(self):
        """test a reverse sorted list of integer"""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_mixed_list(self):
        """test a mixed list of integers"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_empty_list(self):
        """test for empty list"""
        self.assertIsNone(max_integer([]))

    def test_single_element_list(self):
        """test for list contains only one element"""
        self.assertEqual(max_integer([5]), 5)

    def test_negative_numbers(self):
        """test for list of negative numbers"""
        self.assertEqual(max_integer([-1, -3, -4, -2]), -1)

    def test_float_numbers(self):
        """test for list of float numbers"""
        self.assertEqual(max_integer([1.5, 2.7, 3.9, 4.2]), 4.2)

    def test_ints_and_floats(self):
        """test for list contains both integers and floats"""
        self.assertEqual(max_integer([1.53, 15.5, -9, 15, 6]), 15.5)


if __name__ == '__main__':
    unittest.main()
