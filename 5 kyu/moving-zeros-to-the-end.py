'''
	5kyu - Moving Zeros To The End
	https://www.codewars.com/kata/moving-zeros-to-the-end/solutions/python
'''

def move_zeros(array):
    l = 0
    arr = []
    for i in range(0,len(array)):
        if array[i] == 0 and type(array[i]) in (int, float):
            l+=1
        else:
            arr.append(array[i])
    return arr+[0]*l