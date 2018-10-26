'''
	4kyu - Pyramid Slide Down
	https://www.codewars.com/kata/pyramid-slide-down/python
'''

def longest_slide_down(pyramid):
    for i in range(1,len(pyramid)):
        pyramid[i][0] += pyramid[i-1][0]
        for j in range(1,len(pyramid[i])-1):
            pyramid[i][j] += max(pyramid[i-1][j-1],pyramid[i-1][j])
        pyramid[i][len(pyramid[i])-1] += pyramid[i-1][len(pyramid[i-1])-1]
    return max(pyramid[len(pyramid)-1])