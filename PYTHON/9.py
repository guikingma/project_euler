'''
9:
A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,

a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

def execute(p_s):
	a=0
	b=0
	c=0
	s=p_s

	for a in range(1, s/3):
		for b in range(a, s/2):
			c = s - a - b
			#print a, b, c
			if(a*a+b*b==c*c):
				return a*b*c

print execute(1000)