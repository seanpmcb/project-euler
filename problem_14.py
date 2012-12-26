#!/usr/bin/python

'''
Project Euler
Problem 14
http://projecteuler.net/problem=14

The following iterative sequence is defined for the set of positive integers:

n ==> n/2 (n is even)
n ==> 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 ==> 40 ==> 20 ==> 10 ==> 5 ==> 16 ==> 8 ==> 4 ==> 2 ==> 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains
10 terms. Although it has not been proved yet (Collatz Problem), it is thought
that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''

def main():
    num = 1000000
    max_terms = (0, 0)  # num terms, starting

    while num > 1:
        n = int(num)
        num_terms = 0
        while n > 1:
            num_terms += 1
            if n % 2:
                n *= 3
                n += 1
            else:
                n /= 2
        if num_terms > max_terms[0]:
            max_terms = (num_terms, int(num))
        num -= 1
    print max_terms

if __name__ == '__main__':
    main()