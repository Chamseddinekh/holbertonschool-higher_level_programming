#!/usr/bin/python3
"""Unittest"""


import unittest

max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_empty(self):
        self.assertEqual(max_integer([]), None)

    def test_max_end(self):
        self.assertEqual(max_integer([1, 2, 3]), 3)

    def test_max_begin(self):
        self.assertEqual(max_integer([5, 2, 3]), 5)

    def test_negative(self):
        self.assertEqual(max_integer([-6, 7, 8]), 8)

    def test_all_negative(self):
        self.assertEqual(max_integer([-6, -7, -8]), -6)

    def test_one_elem(self):
        self.assertEqual(max_integer([6]), 6)
    
    def test_max_middle(self):
        self.assertEqual(max_integer([1, 5, 3]), 5)

if __name__ == '__main__':
    unittest.main()