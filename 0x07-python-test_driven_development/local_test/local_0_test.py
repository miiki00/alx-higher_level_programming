#!/usr/bin/python3
"""
Test for the function add_integer.
"""
import unittest, os, sys
sys.path.insert(0, os.getcwd() + '/../')
add_integer = __import__('0-add_integer').add_integer


class addIntegerTest(unittest.TestCase):
    def test_add_functionality_and_return_value(self):
        first = [32.89, 32.93, 32, -2, -2, 3]
        second = [32.65, 43, 43.43, 3, -3, -3]

        for k in range(len(first)):
            i = first[k]
            j = second[k]
            self.assertEqual(add_integer(i, j), int(i + j))

    def test_input_validation(self):
        li = [32, 32, 534]
        dic = {32: 32, 2: 32}
        sets = {8932, 32, 3, 32}
        tups = (32, 234, 54, 64)
        stri = "fjdkl"
        lis = [li, dic, sets, tups, stri]
        with self.assertRaises(TypeError):
            add_integer(stri, 32)
        with self.assertRaises(TypeError):
            add_integer(32, li)
