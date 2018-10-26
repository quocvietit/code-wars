'''
	6kyu - Take a Ten Minute Walk
	https://www.codewars.com/kata/take-a-ten-minute-walk/solutions/python
'''

def isValidWalk(walk):
    return len(walk)==10 and walk.count('n') == walk.count('s') and walk.count('w') == walk.count('e')
	
'''
def isValidWalk(walk):
    data = walk
    return 10 == (data.count('n')+data.count('s')+data.count('w')+data.count('e'))
'''