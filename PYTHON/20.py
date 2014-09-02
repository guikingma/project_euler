'''
20
'''

def fat(number):
	ret = 1
	for i in range(2,number+1):
		ret = ret * i
	return ret

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
	print sum_digits(fat(100))

execute()
