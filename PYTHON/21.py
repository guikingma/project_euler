'''
21
'''

def fat(number):
	fats = []
	for i in range(1,int(number/2)+1):
		if number%i==0:
			fats.append(i)
	return fats

def get_amicable(number):
	sum_fats1 = sum(fat(number))
	sum_fats2 = sum(fat(sum_fats1))
	if number == sum_fats2:
		return sum_fats1
	return -1

def is_amicable(number):
	sum_fats1 = sum(fat(number))
	sum_fats2 = sum(fat(sum_fats1))
	if number == sum_fats2:
		return True
	return False


def execute(number):
	list_amicable = range(1,number+1)
	for i in list_amicable:
		amicable_i = get_amicable(i)
		if amicable_i == -1:
			list_amicable.remove(i)
	print list_amicable
	#list_amicable.remove(2)
	#print list_amicable

	#print get_amicable(283)

def execute2(number):
	count = 0
	for i in range(1,number+1):
		pass

execute(50)
