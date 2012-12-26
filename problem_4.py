#!/usr/bin/python

'''
Project Euler
Problem 4
http://projecteuler.net/problem=4

A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91  99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''


def main():
    ''' Limited Brute Force '''
    x = 999
    y = 998
    max_num = 0
    while x > 100:
        while y > 100:
            num = x * y
            if num < max_num:
                break
            str_num = str(num)
            if str_num == str_num[::-1]:
                max_num = num
                break
            y -= 1
        x -= 1
        y = x - 1
    return max_num

if __name__ == '__main__':
    print main()
