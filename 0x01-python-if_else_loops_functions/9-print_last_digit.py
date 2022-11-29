#!/usr/bin/python3

# print_last_digit - prints the last digit of a number
# @number: The number to extract the last digit from
#
# Return: The last digits value.
def print_last_digit(number):
    l_digit = number % 10
    if number < 0 and l_digit != 0:
        l_digit = 10 - l_digit
    print("{:d}".format(l_digit), end="")
    return l_digit
