def slope_fn(grid, rt, dn):
	n = 0
	pos = -1

	for i in range(0, len(grid), dn):
		if pos==-1:
			pos=0
			continue
		pos += rt
		pos = pos%len(grid[i])
		if grid[i][pos]=='#':
			n+=1

	return n

def n_trees(grid):
	sim = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
	total_n = 1

	for i in sim:
		rt, dn = i
		total_n *= slope_fn(grid, rt, dn)

	return total_n




with open('day3_ip.txt', 'r') as f:
	grid = f.read().strip().split('\n')


print(n_trees(grid))