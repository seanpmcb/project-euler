#!/usr/bin/python

'''
Project Euler
Problem 1
http://projecteuler.net/problem=1

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''

i = 1
sum = 0
while i < 1000:
    if not i % 3 or not i % 5:
        sum += i
    i += 1

print sum

'''
Better Way:
s = 0
for i in range(1,1000,1):
    if i%5==0 or i%3==0:
        s += i
print '%g' % s
'''