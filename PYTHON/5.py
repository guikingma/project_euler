'''
5:
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''
import math

def test_number(number, x, y):
	if y<x: #x tem que ser menor do que y
		return false
	it = x
	while it <= y:
		if not number%it==0:
			return False
		it = it + 1
	return True
	pass

def execute(x, y):
	test = y 
	found = test_number(test, x, y)
	while not found:
		test = test + y
		found = test_number(test, x, y)
	return test


print execute(1,20)