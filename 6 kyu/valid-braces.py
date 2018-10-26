'''
	6kyu - Valid Braces
	https://www.codewars.com/kata/valid-braces/solutions/python
'''

def validBraces(string):
    arr = dict()
    for i in string:
        if i == '{':
              arr['}'] = arr.get('}',0)+1
        elif i == '(':
            arr[')'] = arr.get(')',0)+1
        elif i == '[':
              arr[']'] = arr.get(']',0)+1
        elif i == '}':
              arr['}'] = arr.get('}',0)-1
        elif i == ')':
              arr[')'] = arr.get(')',0)-1
        elif i == ']':
              arr[']'] = arr.get(']',0)-1
        if arr.get(']',0) == -1 or arr.get(')',0) == -1 or arr.get('}',0) == -1:
            return False
    return string.count('(') == string.count(')') and string.count('{') == string.count('}') and string.count('[') == string.count(']')