import numpy as np

def displayPathtoPrincess(n, r, c, grid):
	
	grid = [[x for x in k] for k in grid]

	m_pos = (r, c)
	p_pos = [(x,y) for y in range(n) for x in range(n) if grid[x][y] == 'p'][0]

	if m_pos[0] > p_pos[0]:
		return 'UP'
	elif m_pos[0] < p_pos[0]:
		return 'DOWN'

	if m_pos[1] > p_pos[1]:
		return 'LEFT'
	elif m_pos[1] < p_pos[1]:
		return 'RIGHT'


n = 5
r, c = (2, 3)


grid = ['-----', '-----', 'p--m-', '-----', '-----']
print(np.array(grid))
print()

print(displayPathtoPrincess(n, r, c, grid))