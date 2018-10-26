'''
    4kyu - Path Finder #1: can you reach the exit?
    https://www.codewars.com/kata/path-finder-number-1-can-you-reach-the-exit/train/python
'''
def find(matrix, n):
    stack = [(0,0)]
    matrix[0][0] = 'W'
    while(len(stack)):
        x, y = stack[-1]
        stack = stack[:-1]
        if x+1 == n - 1  and y == n-1 or x == n - 1  and y + 1== n-1:
            return True
        
        if x-1 >= 0 and matrix[x-1][y] != 'W':
            matrix[x-1][y] = 'W'
            stack.append(( x-1, y))
            
        if x+1 < n and matrix[x+1][y] != 'W':
            matrix[x+1][y] = 'W'
            stack.append(( x+1, y))
            
        if y-1 >= 0 and matrix[x][y-1] != 'W':
            matrix[x][y-1] = 'W'
            stack.append(( x, y-1))
            
        if y+1 < n and matrix[x][y+1] != 'W':
            matrix[x][y+1] = 'W'
            stack.append(( x, y+1))
        
    return False   
    
def path_finder(maze):
    matrix = []
    maze = maze.split('\n')
    
    for i in maze:
        ma = []
        for j in i:
            ma.append(j)
        matrix.append(ma)
        
    n = len(maze)
    if len(maze) == 1:
        if matrix[0][0] != 'W':
            return True
        else:
            return False
    
    if matrix[n-1][n-1] == 'W' or matrix[0][0] == 'W':
        return False

    return find(matrix, n)
