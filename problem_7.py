#!/usr/bin/python

'''
Project Euler
Problem 7
http://projecteuler.net/problem=7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that
the 6th prime is 13.

What is the 10 001st prime number?
'''


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


def main():
    '''
    Find the 10001st prime number
    '''
    prime_count = 2
    prime_total = 10001
    num = 3
    while prime_count < prime_total:
        num += 2
        if is_prime(num):
            prime_count += 1
    print 'prime # %s is %s' % (prime_count, num)


if __name__ == '__main__':
    main()
