'''
	4kyu - Snail
	https://www.codewars.com/kata/snail/solutions/python
'''

def snail(array):
    arr = []
    l = len(array[0])
    s,n = 0,l-1
    for i in range(0,int(l/2+1)):
        for j in range(0,n-s+1):
            arr.append(array[s][s+j]) 
        for j in range(1,n-s+1):
            arr.append(array[s+j][n])
        for j in range(1,n-s+1):
            arr.append(array[n][n-j]) 
        for j in range(1,n-s):
            arr.append(array[n-j][s])
        s+=1
        n-=1
    return arr