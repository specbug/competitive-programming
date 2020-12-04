def n_trees(grid):
	n = 0
	pos = -1
	for i in grid:
		if pos==-1:
			pos=0
			continue
		pos += 3
		pos = pos%len(i)
		if i[pos]=='#':
			n+=1
	return n


with open('day3_ip.txt', 'r') as f:
	grid = f.read().strip().split('\n')


print(n_trees(grid))