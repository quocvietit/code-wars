'''
	8kyu - Remove First and Last Character Part Two
	https://www.codewars.com/kata/remove-first-and-last-character-part-two/solutions/python
'''
def array(string):
    string = string.split(',')
    return None if len(string) <3 else " ".join(string[1:-1])