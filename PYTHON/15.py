'''
15:
Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20x20 grid?
'''

# --- fatorial function
def fat(x):
	ret = 1
	for i in range(2,x+1):
		ret = ret * i
	return ret

def ways(m, n):
	return fat(m+n)/(fat(m)*fat(n))

def execute():
	print ways(20, 20)


execute()

