'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

'''
#otimizar:

'''


def isPalindrome(p_x):
	str_x = str(p_x)
	len_x = len(str_x)
	if len_x % 2 == 0:
		s1 = str_x[0:len_x/2]
		s2 = str_x[len_x/2:len_x]
		if s1 == s2[::-1]:
			return True
	return False

def all_palindromes_mult(p_x, p_y):
	answer = 0	
	
	for i in range(1,10**p_x):
		for j in range(1,10**p_y):
			mult = i*j
			if isPalindrome(mult):
				if mult > answer:
					answer = mult
	return answer

#print all_palindromes_mult(3,3)



################################################
#
#12?
#o(n)
def triangle_number(p_x):
	answer = 0;
	for i in range(1, p_x+1):
		answer = answer + i
	return answer

#lista primos ate numero p_x
def listprimes(p_x):
	pass

#lista fatores (primos) de numero p_x
def list_factors(p_x):
	factors = []
	for i in listprimes(p_x):
		if p_x%i==0:
			factors.append(i)
	return factors

print triangle_number(7)