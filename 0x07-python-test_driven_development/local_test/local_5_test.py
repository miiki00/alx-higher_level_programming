#!/usr/bin/python3
"""
This is a test for the module 5-text_indentation
"""
import unittest
import os
import sys
sys.path.insert(0, os.getcwd() + '/../')
text_indentation = __import__('5-text_indentation').text_indentation


# if you want to run this test on the function you should first uncomment
# the return statments on the functions
class textIndentationTest(unittest.TestCase):

    def test_functionality(self):

        # test with string with white spaces after and before delimetters
        # and also at the beggining and end of a string.
        testText = """ Lorem ipsum dolor sit amet, consectetur adipiscing \
elit. Quonam modo? Utrum igitur tibi litteram videor an totas paginas \
commovere? Non autem hoc: igitur ne illud quidem. Fortasse id optimum, sed \
ubi illud: Plus semper voluptatis? Teneo, inquit, finem illi videri nihil \
dolere. Transfer idem ad modestiam vel temperantiam, quae est moderatio \
cupiditatum rationi oboediens. Si id dicis, vicimus. Inde sermone vario sex \
illa a Dipylo stadia confecimus. Sin aliud quid voles, postea. Quae animi \
affectio suum cuique tribuens atque hanc, quam dico. Utinam quidem dicerent \
alium alio beatiorem! Iam ruinas videres      """
        expected = """Lorem ipsum dolor sit amet, consectetur adipiscing elit.

Quonam modo?

Utrum igitur tibi litteram videor an totas paginas commovere?

Non autem hoc:

igitur ne illud quidem.

Fortasse id optimum, sed ubi illud:

Plus semper voluptatis?

Teneo, inquit, finem illi videri nihil dolere.

Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum \
rationi oboediens.

Si id dicis, vicimus.

Inde sermone vario sex illa a Dipylo stadia confecimus.

Sin aliud quid voles, postea.

Quae animi affectio suum cuique tribuens atque hanc, quam dico.

Utinam quidem dicerent alium alio beatiorem! Iam ruinas videres"""
        self.assertMultiLineEqual(text_indentation(testText), expected)

        # test with empty string
        testText = ""
        expected = ""
        self.assertMultiLineEqual(text_indentation(testText), expected)

        # test with string containing only white space.
        testText = "                    "
        expected = ""
        self.assertMultiLineEqual(text_indentation(testText), expected)

        # test with string containing newline feed surrounded by white space.
        testText = "       \n       "
        expected = "\n"
        self.assertMultiLineEqual(text_indentation(testText), expected)

        # test with a string that have no delimeters.
        testText = "this string have no delimeters"
        expected = "this string have no delimeters"
        self.assertMultiLineEqual(text_indentation(testText), expected)

        # test with a string with no delimeter surrounded by space.
        testText = "  this string have no delimeter    "
        expected = "this string have no delimeter"
        self.assertMultiLineEqual(text_indentation(testText), expected)

        # test with a string containing sequence of delimeters.
        testText = "?.:?"
        expected = "?\n\n.\n\n:\n\n?\n\n"
        self.assertMultiLineEqual(text_indentation(testText), expected)

        # test with a stirng containing sequence of delimetes and small words.
        testText = "??ss.m::   .s   "
        expected = "?\n\n?\n\nss.\n\nm:\n\n:\n\n.\n\ns"
        self.assertMultiLineEqual(text_indentation(testText), expected)

    def test_input_validation(self):

        # test with non string object
        testObject = ("non string object",)
        with self.assertRaises(TypeError):
            text_indentation(testObject)


if __name__ == '__main__':
    unittest.main()
