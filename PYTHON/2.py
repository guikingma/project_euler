'''
2:
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
'''

def fib(n):
	x1 = 0
	x2 = 1
	xn = 0
	soma = 0
	for i in range(n):
		xn = x1+x2
		x1=x2
		x2=xn
		if (xn%2==0) and (xn < 4000000):
			#print xn
			soma = soma + xn
	print soma


fib(100)