#!/usr/bin/python

'''
Project Euler
Problem 3
http://projecteuler.net/problem=3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''
from random import randint
from fractions import gcd

# Original
# def original(number):
#     factor = 1
#     factors = []
#     while number != 1:
#         factor += 1
#         if number % factor:
#             continue
#         factors.append(factor)
#         number /= factor
#     return max(factors)

# Better way - Pollard Rho


def pollard_rho(N):
    '''
    Find a random prime factor of an integer using Pollard Rho factorization

    Args: An integer

    Returns: an integer
    '''


    def f(x):
        '''
        Polynomial function for creating pseudo random numbers

        Args: x - and integer

        Returns: an integer
        '''
        pass


def random_factor_method(number):
    factors = set()
    factor = 1
    while number > factor:
        factor = pollard_rho(number)
        number /= factor
        factors.append(factor)
    return max(factors)


def main():
    loops = 1
    while loops:
        number = 600851475143
        # answer = original(number)
        answer = random_factor_method(number)
        loops -= 1
    print answer

if __name__ == '__main__':
    main()
