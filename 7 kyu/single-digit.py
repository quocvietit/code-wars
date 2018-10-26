'''
	7kyu - Single digit
	https://www.codewars.com/kata/single-digit/train/python
'''

def single_digit(n):
    sum = 0
    if n < 10:
        return n
    while n>0:
        sum+=n%2
        n//=2
    return single_digit(sum)