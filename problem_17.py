#!/usr/bin/python

'''
Project Euler
Problem 17
http://projecteuler.net/problem=17

If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in
words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20
letters. The use of "and" when writing out numbers is in compliance with
British usage.
'''

conversions = {
    0: '',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
    100: 'hundred',
    1000: 'thousand'
}


def spell_number(num):
    spelt_number = 'onethousand'
    if num < 21:
        return conversions[num]
    elif num < 100:
        (tens, units) = divmod(num, 10)
        spelt_number = conversions[tens*10]
        spelt_number += conversions[units]
    elif num < 1000:
        (div, mod) = divmod(num, 100)
        spelt_number = conversions[div] + 'hundred'
        if mod > 0:
            spelt_number += 'and'
            spelt_number += spell_number(mod)
    return spelt_number


def main():
    num = 1000
    spelt_numbers = ''
    for i in range(1, num + 1):
        spelt_numbers += spell_number(i)
    print len(spelt_numbers)

if __name__ == '__main__':
    main()