'''
3:
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
'''
import math

def is_prime(number):
	#small_number = int(math.ceil(number**.5))
	small_number = number
	i=3
	while i<small_number:
		if (number%i==0):
			return False
		i = i + 2
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

def fat(number):
	fat_list=[]
	fat_num=1
	fat_num = next_prime(fat_num)
	while (fat_num < int(math.ceil(number**.5))):
		#print fat_num
		while (number % fat_num == 0):
			#print 'oi'
			if (is_prime(fat_num)):
				fat_list.append(fat_num)		
			fat_num = next_prime(fat_num)
		fat_num = next_prime(fat_num)	
	return fat_list
	pass

print fat(600851475143)
print is_prime(16)