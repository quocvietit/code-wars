'''
	7kyu - Ones and Zeros
	https://www.codewars.com/kata/ones-and-zeros/solutions/python
'''

def binary_array_to_number(arr):
    arr = arr[::-1]
    return sum(arr[i]*2**i for i in range(0,len(arr)))