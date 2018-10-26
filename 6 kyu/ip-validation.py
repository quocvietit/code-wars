'''
	6kyu - IP Validation
	https://www.codewars.com/kata/ip-validation/solutions/python
'''

def is_valid_IP(strng):
    return len(strng.split('.')) ==4  and all(i.isdigit() and i==str(int(i)) and int(i)<=255 for i in strng.split('.'))