#!/usr/bin/python

'''
Project Euler
Problem 15
http://projecteuler.net/problem=15

Starting in the top left corner of a 2x2 grid, there are 6 routes (without
backtracking) to the bottom right corner.

How many routes are there through a 20x20 grid?
'''

import sys

def main(side_length):
    '''
    calculate the number of routes for a grid of size side_length x side_length
    '''
    # Depth first search
    pass

if __name__ == '__main__':
    main(int(sys.argv[1]))