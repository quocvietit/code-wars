'''
	7kyu - Disemvowel Trolls
	https://www.codewars.com/kata/disemvowel-trolls/train/python
'''

def disemvowel(string):
    string = string.replace('i','')
    string = string.replace('o','')
    string = string.replace('u','')
    string = string.replace('e','')
    string = string.replace('a','')
    string = string.replace('I','')
    string = string.replace('O','')
    string = string.replace('U','')
    string = string.replace('E','')
    string = string.replace('A','')
    return string