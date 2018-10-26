'''
	6kyu - Bit Counting
	https://www.codewars.com/kata/bit-counting/solutions/python
'''

def countBits(n):
    return sum(int(i) for i in format(n,'b'))