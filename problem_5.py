#!/usr/bin/python

'''
Project Euler
Problem 5
http://projecteuler.net/problem=5

A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91  99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

import sys


def main(num):
    '''
    Find the smallest positive number that is evenly divisible by all the
    numbers less than a given number
    '''
    print "Finding the lowest common multiple for numbers 1 to %s" % (num)
    numbers = range(num - 1, num / 2, -1)
    multiple = num
    step = num
    for number in numbers:
        while multiple % number:
            multiple += step
        step = multiple
    print multiple


if __name__ == '__main__':
    main(int(sys.argv[1]))
