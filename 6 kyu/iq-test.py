'''
	6kyu - IQ Test
	https://www.codewars.com/kata/iq-test/solutions/python
'''

def iq_test(numbers):
    data = list(map(int,numbers.split(" ") ))
    if len(data)==1:
        return int(data)
    di = dict()
    dt = []
    for i in data:
        dt.append(i%2)
        di[i%2]=di.get(i%2,0)+1
    di[0] = 0
    if di[1] == 1:
        di[0] = di[1]
    return dt.index(di[0])+1