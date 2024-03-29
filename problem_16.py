#!/usr/bin/python

'''
Project Euler
Problem 16
http://projecteuler.net/problem=16

2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2**1000?
'''

def main():
	num = 2**1000
	sum = 0
	for digit in str(num):
		sum += int(digit)
	print sum

if __name__ == '__main__':
    main()