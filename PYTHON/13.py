'''
13:
Work out the first ten digits of the sum of the following one-hundred 50-digit numbers
'''

def to_int(p_list):
	retorno = []
	str_number = '9998'
	int_number = 0
	i = 0
	while i < len(p_list):
		str_number = p_list[i]
		if not (i==len(p_list)-1):
			str_number = str_number[0:-1]
		#print str_number
		if str_number.isdigit():
			int_number = int(str_number)
			retorno.append(int_number)
		else:
			print 'Error: contains digit'
			retorno.append(0)
		i = i + 1
	return retorno

def return_numbers(p_file):
	fopen = open(p_file, 'r')
	return to_int(fopen.readlines())

def sum_list(p_list):
	soma = 0
	for i in p_list:
		soma = soma + i
	return soma

def execute():
	print str(sum_list(return_numbers('13.file')))[0:10]

execute()
#print_list(return_numbers('13.file'))
