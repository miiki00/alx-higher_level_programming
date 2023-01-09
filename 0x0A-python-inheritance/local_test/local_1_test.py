#!/usr/bin/python3
"""
This is a unittest for the function(s) in the module '1-my_list'
"""
import sys
import os
import unittest
sys.path.insert(0, os.getcwd() + '/../')
MyList = __import__('1-my_list').MyList


# if you want to run this test on the function you should first uncomment
# the return statments on the functions.
class test_My_list(unittest.TestCase):

    def test_functionality(self):
        # test with completly descending ordered list of integer.
        testListInit = [10, 8, 6, 4, 2, 0]
        testList = MyList()
        for i in testListInit:
            testList.append(i)
        expected = [0, 2, 4, 6, 8, 10]
        self.assertEqual(testList.print_sorted(), expected)

        # test with a list with nothing to be changes(ordered list).
        testListInit = [0, 2, 4, 6, 8, 10]
        testList = MyList()
        for i in testListInit:
            testList.append(i)
        expected = [0, 2, 4, 6, 8, 10]
        self.assertEqual(testList.print_sorted(), expected)

        # test with a completly randomized list.
        testListInit = [83, 543, 65, 224, 64, 76, 87]
        testList = MyList()
        for i in testListInit:
            testList.append(i)
        expected = [64, 65, 76, 83, 87, 224, 543]
        self.assertEqual(testList.print_sorted(), expected)


if __name__ == "__main__":
    unittest.main()
