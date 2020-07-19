import numpy as np

def next_move(posr, posc, board):
	
	n = 5

	# board = [[x for x in k] for k in board]

	m_pos = (posr, posc)
	p_pos = [(x,y) for y in range(n) for x in range(n) if board[x][y] == 'd'][0]

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

posr = 0
posc = 0
n = 5

board = ['b---d', '-----', '-----', '-----', '-----']

board = [[x for x in k] for k in board]

print(np.array(board))
print()

n_cleaned = 0

for _ in range(200):

	movement = next_move(posr, posc, board)

	if movement == 'DOWN':
		posr += 1
	elif movement == 'UP':
		posr -= 1
	elif movement == 'RIGHT':
		posc += 1
	elif movement == 'LEFT':
		posc -= 1
	else:
		board[posr][posc] = '-'
		board[np.random.choice(n)][np.random.choice(n)] = 'd'
		n_cleaned += 1

		print(posr, posc)
		print(np.array(board))
		print()

print(n_cleaned)