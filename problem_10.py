#!/usr/bin/python

'''
Project Euler
Problem 10
http://projecteuler.net/problem=10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

import sys


def is_prime(num):
    '''
    Check to see if a number is prime

    Args:
        num the integer we're checking

    Returns:
        True if the integer is prime, False otherwise
    '''
    if not num % 2:
        return False
    max_divisor = int(num ** 0.5) + 1
    for divisor in range(3, max_divisor, 2):
        if not num % divisor:
            return False
    return True


def main(num):
    ''' Find the sum of all the primes below a given number '''
    sum_primes = 2
    for i in range(3, num):
        if is_prime(i):
            sum_primes += i
    print sum_primes

if __name__ == '__main__':
    main(int(sys.argv[1]))
