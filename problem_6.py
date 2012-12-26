#!/usr/bin/python

'''
Project Euler
Problem 6
http://projecteuler.net/problem=6

The sum of the squares of the first ten natural numbers is,
    1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
    (1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.
'''

import sys


# brute force
def main(num):
    ''' Find the difference between the sum of the squares for a given number
    and the square of the sums. '''
    sum_squared = sum(range(1, num + 1, 1))
    sum_squared *= sum_squared
    sum_squares = 0
    for number in range(1, num + 1, 1):
        sum_squares += number * number
    print sum_squared - sum_squares

if __name__ == '__main__':
    main(int(sys.argv[1]))