'''
	7kyu - Sum of two lowest positive integers
	https://www.codewars.com/kata/sum-of-two-lowest-positive-integers/solutions/python
'''

def sum_two_smallest_numbers(numbers):
    return sorted(numbers)[0] + sorted(numbers)[1]