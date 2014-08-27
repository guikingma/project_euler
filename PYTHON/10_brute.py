'''
10:
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
'''
import math

def is_prime_2(n):
	for i in range (2,n):
		if n%i == 0:
			return False
	return True

def is_prime(number):
	#small_number = int(math.ceil(number**.5))
	small_number = number
	i=2
	while i<small_number:
		if (number%i==0):
			return False
		i = i + 1
	return True

def next_prime(number):
	it = number+1
	while not(is_prime(it)):
		it = it + 1
	return it

def primes_before(number):
	print 2
	cont = 3
	while cont < number:
		if is_prime(cont):
			print cont
		cont = cont + 2

def sum_primes_before(number):
	soma = 2
	cont = 3
	while cont < number:
		if is_prime(cont):
			soma = soma + cont
		cont = cont + 2
	return soma

def generate_primes(number):
	prime = 1
	i = 0
	while i<number:
		#print prime
		prime = next_prime(prime)
		i=i+1
	return prime

print sum_primes_before(100000)



