'''
	7kyu - Cat Years, Dog Years (2)
	https://www.codewars.com/kata/cat-years-dog-years-2/train/python
'''

def owned_cat_and_dog(cat_years, dog_years):
    return [cal(cat_years,15,9,4), cal(dog_years,15,9,5)]

def cal(years,first_year, second_year, after_year):
    age = 0
    if years >= first_year:
        age+=1
    years-=first_year
    if years >= second_year:
        age+=1
    years-=second_year
    if years >= after_year:
        age += years//after_year
    return age