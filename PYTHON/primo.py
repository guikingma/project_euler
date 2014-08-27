import math

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
	cont = 3
	while cont < number:
		if is_prime(cont):
			print cont
		cont = cont + 2


def mark(number, crivo):
	len_crivo = len(crivo)
	i=number
	while i < len_crivo-number:
		i = i + number
		if crivo[i]:
			crivo[i] = False
	return crivo

def exec_crivo(number):
	crivo = [True for x in xrange (number+1)] #testar xrange e range
	crivo[0]=False
	crivo[1]=False

	len_crivo = len(crivo)+1
	#print ':' + 

	i=2
	while i <= int(math.ceil(number**.5)):
		crivo_ = mark(i,crivo)
		i = i + 1
	return crivo

def print_crivo(crivo):
	i=0
	while i<len(crivo):
		if crivo[i] == True:
			print i
		i = i + 1

def return_primes(crivo):
	primes = []
	i=0
	while i<len(crivo):
		if crivo[i] == True:
			primes.append(i)
		i = i + 1
	return primes


def sum_crivo(crivo):
	i=0
	soma=0
	while i<len(crivo):
		if crivo[i] == True:
			soma = soma + i
		i = i + 1	
	return soma


#mark(2, crivo)
#mark(3, crivo)

#print crivo

#print_crivo(crivo)
#print sum_crivo(crivo)