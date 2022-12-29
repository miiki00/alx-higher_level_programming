#!/usr/bin/python3
"""
test for the function say_my_name.
"""
import unittest
import os
import sys
sys.path.insert(0, os.getcwd() + '/../')
say_my_name = __import__('3-say_my_name').say_my_name


# if you want to run this test on the function you should first uncomment
# the return statments on the functions
class SayMyNameTest(unittest.TestCase):
    # test for correct functionality given valid input.
    def test_functionality(self):
        # one character.
        firstName = "q"
        lastName = 'd'
        expected = "My name is q d"
        self.assertEqual(say_my_name(firstName, lastName), expected)
        # one argument test
        firstName = "name"
        expected = "My name is name "
        self.assertEqual(say_my_name(firstName), expected)
        # two arguments
        firstName = "Your"
        lastName = "Name"
        expected = "My name is Your Name"
        self.assertEqual(say_my_name(firstName, lastName), expected)

    def test_input_validation(self):
        # test with both non string argument.
        firstName = 233
        lastName = ("string",)
        with self.assertRaises(TypeError):
            say_my_name(firstName, lastName)
        # test with a single non string argument.
        firstName = {"string"}
        with self.assertRaises(TypeError):
            say_my_name(firstName)
        # test with first_name string and last_name non string.
        firstName = "string"
        lastName = ["string"]
        with self.assertRaises(TypeError):
            say_my_name(firstName, lastName)
        # test with first_name non string and last_name string.
        firstName = ("fjklds",)
        lastName = "string"
        with self.assertRaises(TypeError):
            say_my_name(firstName, lastName)


if __name__ == "__main__":
    unittest.main()
