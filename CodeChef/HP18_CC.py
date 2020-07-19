import numpy as np

def rem_elem_list(l, m, n, k):
	c = 0
	temp_l = []
	for i in range(1, int(np.sqrt(max(l)))):
		if i%m==0:
			g = n
			while i*g <= l:
	return l, c

t = int(input())
for _ in range(t):
	n, a, b = map(int, input().split())
	l = list(map(int, input().split()))
	flag = True
	turn = 0
	winner = -1
	while(flag):
		if turn==0:
			l, temp_c =  rem_elem_list(l, a, b, 0)
			if temp_c == 0:
				l, temp_c = rem_elem_list(l, a, 1, 1)
				if temp_c == 0:
					flag=False
					winner = 1
			turn = 1
		elif turn == 1:
			l, temp_c = rem_elem_list(l, b, a, 0)
			if temp_c == 0:
				l, temp_c = rem_elem_list(l, b, 1, 1)
				if temp_c == 0:
					flag=False
					winner=0
			turn = 0

	if winner==0:
		print('BOB')
	elif winner==1:
		print('ALICE')
	else:
		print('WTF')