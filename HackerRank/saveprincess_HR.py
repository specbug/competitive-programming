import numpy as np

def displayPathtoPrincess(n,grid):
	
	grid = [[x for x in k] for k in grid]

	pos_tuple = [(grid[x][y], x,y) for y in range(n) for x in range(n) if grid[x][y] in ['m', 'p']]

	m_pos, p_pos = sorted(list(pos_tuple), key=lambda x: list(x)[0])

	m_pos = tuple(list(m_pos)[1:])
	p_pos = tuple(list(p_pos)[1:])

	path = []

	if m_pos[0] > p_pos[0]:
		path += ['UP']*(m_pos[0] - p_pos[0])
	else:
		path += ['DOWN']*(p_pos[0] - m_pos[0])

	if m_pos[1] > p_pos[1]:
		path += ['LEFT']*(m_pos[1] - p_pos[1])
	else:
		path += ['RIGHT']*(p_pos[1] - m_pos[1])

	for p in path:
		print(p)


n = 3

grid = ['p--', '-m-', '---']
print(np.array(grid))
print()

displayPathtoPrincess(n, grid)