import numpy as np

def next_move(posx, posy, dimx, dimy, board):

	# board = [[x for x in k] for k in board]

	m_pos = (posx, posy)
	p_pos = [(x,y) for y in range(dimy) for x in range(dimx) if board[x][y] == 'd']

	p_pos = sorted(p_pos, key=lambda x: abs(x[0]-posx)+abs(x[1]-posy))[0]

	if m_pos == p_pos:
		print('CLEAN')
		return 'CLEAN'

	else:
		if m_pos[0] > p_pos[0]:
			print('UP')
			return 'UP'
		elif m_pos[0] < p_pos[0]:
			print('DOWN')
			return 'DOWN'
		elif m_pos[1] > p_pos[1]:
			print('LEFT')
			return 'LEFT'
		elif m_pos[1] < p_pos[1]:
			print('RIGHT')
			return 'RIGHT'

posx = 0
posy = 0
dimx = 5
dimy = 5

board = ['b---d', '-d--d', '--dd-', '--d--', '----d']

board = [[x for x in k] for k in board]

print(np.array(board))
print()

n_moves = 0

while True:
	
	if sum([1 for i in board for j in i if j == 'd']) == 0:
		break

	movement = next_move(posx, posy, dimx, dimy, board)

	if movement == 'DOWN':
		posx += 1
	elif movement == 'UP':
		posx -= 1
	elif movement == 'RIGHT':
		posy += 1
	elif movement == 'LEFT':
		posy -= 1
	else:
		board[posx][posy] = '-'

	n_moves += 1

print(n_moves)
print()
print(posx, posy)
print()
print(board)