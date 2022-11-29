#!/usr/bin/python3

# fizzbuzz - prints number form 1 to 100 and replaces multiple of 3 by Fizz
# multiples of 5 by Buzz and multiple of both with FizzBuzz.
# Return: Void(None)
def fizzbuzz():
    fizz = "FizzBuzz"
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("{:s}".format(fizz), end=" ")
        elif i % 3 == 0:
            print("{:s}".format(fizz[:4]), end=" ")
        elif i % 5 == 0:
            print("{:s}".format(fizz[4:]), end=" ")
        else:
            print("{:d}".format(i), end=" ")
