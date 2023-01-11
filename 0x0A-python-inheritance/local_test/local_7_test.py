#!/usr/bin/python3
"""
unittest for the module '7-base_geometry'
"""
import unittest
import os
import sys
sys.path.insert(0, os.getcwd() + '/../')
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class testBaseGeometry(unittest.TestCase):
    # testing functionlaity of the method.
    def test_functionality(self):
        # the object to test with.
        testObj = BaseGeometry()

        # test with simple valid inputs.
        testName = "width"
        testValue = 23
        self.assertIsNone(testObj.integer_validator(testName, testValue))

    # testing how the method handles invalid inputs.
    def test_input_validation(self):
        # the object to test with.
        testObj = BaseGeometry()

        # test with negative value
        testName = "width"
        testValue = -23
        with self.assertRaises(ValueError):
            testObj.integer_validator(testName, testValue)

        # test with non number input.
        testName = "width"
        testValue = "string"
        with self.assertRaises(TypeError):
            testObj.integer_validator(testName, testValue)
