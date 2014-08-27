'''
6:
The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''
import math

def calc_1(number):
	soma = 0
	i = 0
	while i <= number:
		soma=soma+i*i
		i = i + 1
	return soma

def calc_2(number):
	soma = 0
	i = 0
	while i <= number:
		soma=soma+i
		i = i + 1
	return soma*soma

def execute(number):
	return calc_2(number)-calc_1(number)

print execute(100)