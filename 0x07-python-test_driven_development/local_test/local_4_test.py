#!/urs/bin/python3
"""
This is a unittest for the function(s) in the module 4-print_square
"""

import unittest
import os
import sys
sys.path.insert(0, os.getcwd() + '/../')
print_square = __import__('4-print_square').print_square


# if you want to run this test on the function you should first uncomment
# the return statments on the functions.
class printSquareTest(unittest.TestCase):
    def test_functionality(self):

        # test with input 0
        testSize = 0
        self.assertIsNone(print_square(testSize))

        # test with input 1
        testSize = 1
        expected = '#'
        result = print_square(testSize)
        self.assertMultiLineEqual(result, expected)

        # test with positive integer
        testSize = 4
        expected = '####\n####\n####\n####'
        self.assertMultiLineEqual(print_square(testSize), expected)

        # test with a positive float
        testSize = 3.2
        expected = "###\n###\n###"
        self.assertMultiLineEqual(print_square(testSize), expected)

    def test_input_validation(self):

        # test with negative int
        # expected to raise a ValueError.
        testObject = -1
        with self.assertRaises(ValueError):
            print_square(testObject)

        # test with negative float.
        # expectedd to raise a TypeError.
        testObject = -1.3
        with self.assertRaises(TypeError):
            print_square(testObject)

        # test with non number object.
        # expected to raise a TypeError.
        testObject = "string"
        with self.assertRaises(TypeError):
            print_square(testObject)


if __name__ == "__main__":
    unittest.main()
