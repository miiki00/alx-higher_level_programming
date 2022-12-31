#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_functionality(self):
        # test with empty list.
        testList = []
        self.assertIsNone(max_integer(testList))

        # test with list with one element.
        testList = [32]
        expected = 32
        self.assertEqual(max_integer(testList), expected)

        # test with list with same elements
        testList = [32, 32, 32, 32]
        expected = 32
        self.assertEqual(max_integer(testList), expected)

        # test with normal input
        testList = [1, 2, 4, 3]
        expected = 4
        self.assertEqual(max_integer(testList), expected)


if __name__ == "__main__":
    unittest.main()
