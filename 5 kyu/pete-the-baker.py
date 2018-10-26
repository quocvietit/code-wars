'''
	5kyu - Pete, the baker
	https://www.codewars.com/kata/pete-the-baker/solutions/python
'''

def cakes(recipe, available):
    l = 0
    for key in recipe:
        if key in available:
            s = int(available[key]/recipe[key])
            if l == 0:
                l = s
            l = min(s,l)
            if s == 0:
                break
        else:
            l = 0 
            break
    return l