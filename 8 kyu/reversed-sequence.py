'''
	8kyu - Reversed sequence
	https://www.codewars.com/kata/reversed-sequence/train/python
'''
def reverse_seq(n):
    arr = [i+1 for i in range(n)]
    return arr[::-1]