'''
16:
2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of the number 2**1000?
'''

def sum_digits(number):
	tnumber = number
	#tnumber = tnumber/10
	soma = 0
	resto = 0
	while tnumber > 0:
		resto = tnumber%10
		soma = soma + resto
		tnumber = tnumber/10
	return soma

def execute():
	print sum_digits(2**1000)


execute()
