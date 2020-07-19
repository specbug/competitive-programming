import numpy as np

t = int(input())
for _ in range(t):
	r, c, k = map(int, input().split())
	lr = 99
	lc = 99
	ur = 0
	uc = 0
	c=0
	for i in range(1, 9):
		tr = np.abs(r-i)
		trr = np.abs(r+i)
		if tr <= k and tr < lr:
			lr = tr
		if trr <
		tc = np.abs(c-i)
		tcc = np.abs(c+i)
		if tc <= k and tc < cc:
			lc = tc
	for i in range(r, 9):
		for j in range(cc)
		c+=1
