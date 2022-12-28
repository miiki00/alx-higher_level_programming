#!/usr/bin/python3
"""
Test for the function add_integer.
"""
import unittest
import os
import sys
sys.path.insert(0, os.getcwd() + '/../')
matrix_divided = __import__('2-matrix_divided').matrix_divided


class matrixDividedTest(unittest.TestCase):
    def test_add_functionality(self):
        # empty list test
        testList = []
        expected = testList
        self.assertEqual(matrix_divided(testList, 2), expected)
        # list containing empty lists
        testList = [[], [], []]
        expected = testList
        self.assertEqual(matrix_divided(testList, 2.3), expected)
        # a valid input list.
        testList = [[32, 34.2, 64.2],
                    [2, 53.2, 65],
                    [43, 65.5, 76.1]]
        expected = [[16.0, 17.1, 32.1],
                    [1.0, 26.6, 32.5],
                    [21.5, 32.75, 38.05]]
        self.assertEqual(matrix_divided(testList, 2), expected)
        # a valid input list divided by 1.
        # the return value should be the values them selves
        # but with 2 decimal places.
        testList = [[32, 34.2, 64.2],
                    [2, 53.2, 65],
                    [43, 65.5, 76.1]]
        expected = [[32.0, 34.2, 64.2],
                    [2.0, 53.2, 65.0],
                    [43, 65.5, 76.1]]
        self.assertEqual(matrix_divided(testList, 1), expected)
        # a list containing a list wiht one element.
        testList = [[4]]
        expected = [[2.0]]
        self.assertEqual(matrix_divided(testList, 2), expected)

    def test_input_validation(self):
        # passing a none list object to matrix parameter.
        # expected to rasise a TypeError
        testObject = "string"
        div = 2
        with self.assertRaises(TypeError):
            matrix_divided(testObject, div)
        # passing a list containing different objects
        # expcted to raise a TypeError
        testObject = [[32, 34, 54], "string", 32, 5]
        with self.assertRaises(TypeError):
            matrix_divided(testObject, div)
        # passing a list containing lists with different row.
        # expected to raise a TypeError
        testObject = [[32, 35, 757, 45, 76],
                      [32, 43, 56, 76],
                      [54, 675, 4]]
        with self.assertRaises(TypeError):
            matrix_divided(testObject, div)
        # passing a list containg lists with different objects
        # by different object other that float and integer.
        # expected to raise a TypeError.
        testObject = [[54, 65.5, 76],
                      [54, 76, 87.4],
                      [32, 43.5, "string"]]
        with self.assertRaises(TypeError):
            matrix_divided(testObject, div)
        # passing a valid list and passing div pram a stirng.
        # expected to raise a typeError
        testObject = [[32, 34.2, 64.2],
                      [2, 53.2, 65],
                      [43, 65.5, 76.1]]
        div = "string"
        with self.assertRaises(TypeError):
            matrix_divided(testObject, div)
        # passing a valid list and passing div param 0
        # expect to raise a zeroDivisionError.
        div = 0
        with self.assertRaises(ZeroDivisionError):
            matrix_divided(testObject, div)


if __name__ == "__main__":
    unittest.main()
