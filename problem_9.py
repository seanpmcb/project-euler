#!/usr/bin/python

'''
Project Euler
Problem 9
http://projecteuler.net/problem=9

A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,

a**2 + b**2 = c**2
For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

import sys


def main(pyth_sum):
    ''' find the Pythagorean triplet for which a + b + c = 1000

    a + b + c = pyth_sum
    a = pyth_sum - c - b

    a**2 + b**2 = c**2
    b**2 = c**2 - a**2
    b = ((c**2) - (a**2))**0.5

    a = pyth_sum - c - (((c**2) - (a**2))**0.5)

    '''

    for c in range(1, pyth_sum):
        for a in range(1, c):
            if a == pyth_sum - c - (((c**2) - (a**2))**0.5):
                b = pyth_sum - a - c
                print a * b * c
                sys.exit(0)

if __name__ == '__main__':
    main(int(sys.argv[1]))
