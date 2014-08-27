'''
#main
a = []
a.append([3])
a.append([7,4])
a.append([2,4,6])
a.append([8,5,9,3])
print adj_b(a,2,2)
'''

def get_value(p_list, p_i, p_j):
	try:
		return p_list[p_i][p_j]
	except:
		return -1

def adj(p_list, p_i, p_j):
	try:
		a = p_list[p_i+1][p_j]
		b = p_list[p_i+1][p_j+1]
		return [a, b]
	except:
		return -1

def adj_a(p_list, p_i, p_j):
	try:
		return p_list[p_i+1][p_j]
	except:
		return -1

def adj_b(p_list, p_i, p_j):
	try:
		return p_list[p_i+1][p_j+1]
	except:
		return -1

# --- retorna maior custo em uma lista de listas.
def large_sum(p_list_list):
	best_sum = [-1, -1]
	i = 0
	for p_list in p_list_list:
		this_sum = sum(p_list)
		if (this_sum > best_sum[1]):
			best_sum = [i,this_sum]
		i = i + 1
	return best_sum
'''
ways = [[11,11,11,11,11], [1,2,3,4,5], [2,3,4,5,6], [3,4,5,6,7], [9,9,9,9,9], [1,1,1,1,1], [10,10,10,10,10]]
print large_sum(ways)
print ways[large_sum(ways)[0]]
'''
a = []
a.append([3])
a.append([7,4])
a.append([2,4,6])
a.append([8,5,9,3])


#a[len(a)-2][len(a)-2]==6


def all_paths(p_triangle, p_i, p_j):
	current = p_triangle[p_i][p_j]
	if p_i < len(p_triangle) - 1:
		below_paths = all_paths(p_triangle, p_i+1, p_j) + all_paths(p_triangle, p_i+1, p_j+1)
		#print below_paths
		print [[current] + path for path in below_paths]
		return [[current] + path for path in below_paths]
	else:
		print '.'
		return [[current]]

all_paths(a, 0, 0)