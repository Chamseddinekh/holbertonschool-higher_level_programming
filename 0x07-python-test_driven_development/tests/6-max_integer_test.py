#!/usr/bin/python3
"""Unittest"""


import unittest

max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_empty(self):
        self.assertEqual(max_integer([]), None)


if __name__ == '__main__':
    unittest.main()