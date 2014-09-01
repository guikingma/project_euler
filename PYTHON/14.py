'''

The following iterative sequence is defined for the set of positive integers:

n = n/2 (n is even)
n = 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 = 40 = 20 = 10 = 5 = 16  8 = 4 = 2 = 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

http://andrefsp.wordpress.com/2011/08/21/project-euler-and-solving-problem-14/
http://code.jasonbhill.com/c/project-euler-problem-14/
'''


def function_rec(p_n, p_count):
	if p_n % 2 == 0:
		print 2
		p_count = p_count + 1
		
		function_rec(p_n/2, p_count)
	else:
		print 3
		p_count = p_count + 1
		function_rec(3*p_n+1, p_count)


def function(p_n):
	if p_n % 2 == 0:
		return p_n/2
	else:
		return (p_n*3)+1

def chain(p_n):
	count = 1
	next = function(p_n)
	#print next
	while next != 1:
		next = function(next)
		#print next
		count = count+1
	count = count + 1
	return count

def longest_chain(p_n):
	longest = p_n
	longest_len = 0
	for i in range(1,p_n+1):
		#print i
		n_len = chain(i)
		if n_len > longest_len:
			longest_len = n_len
			longest = i
	return longest


print longest_chain(1000000)