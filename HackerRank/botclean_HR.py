import numpy as np

def next_move(posr, posc, board):
	
	n = 5

	board = [[x for x in k] for k in board]

	m_pos = (posr, posc)
	p_pos = [(x,y) for y in range(n) for x in range(n) if board[x][y] == 'd']

	p_pos = sorted(p_pos, key=lambda x: abs(x[0]-posr)+abs(x[1]-posc))[0]

	if m_pos == p_pos:
		print('CLEAN')
		# return 'CLEAN'

	else:
		if m_pos[0] > p_pos[0]:
			print('UP')
			# return 'UP'
		elif m_pos[0] < p_pos[0]:
			print('DOWN')
			# return 'DOWN'
		elif m_pos[1] > p_pos[1]:
			print('LEFT')
			# return 'LEFT'
		elif m_pos[1] < p_pos[1]:
			print('RIGHT')
			# return 'RIGHT'

posr = 1
posc = 1

board = ['-----', '-b---', '---d-', '---d-', '--d-d']

board = [[x for x in k] for k in board]

n_moves = 0

while True:
	
	if sum([1 for i in board for j in i if j == 'd']) == 0:
		break

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

	n_moves += 1

print(n_moves)
print()
print(posr, posc)
print()
print(board)


