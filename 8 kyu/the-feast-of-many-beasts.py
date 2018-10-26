'''
	8kyu - The Feast of Many Beasts
	https://www.codewars.com/kata/the-feast-of-many-beasts/solutions/java
'''
def feast(beast, dish):
    return beast[0] == dish[0] and beast[-1] == dish[-1]