import sys

def calc_max_arr(arr, s, e, k, lat=True):
	max_arr = [a[:] for a in arr[:]]
	m = len(max_arr)
	n = len(max_arr[0])
	if lat:
		for r in range(1, m-1):
			for c in range(s, e, k):
        max_arr[r][c] = max(max_arr[r][c], max_arr[r][c-k])
	else:
		for c in range(1, n-1):
			for r in range(s, e, k):
				max_arr[r][c] = max(max_arr[r][c], max_arr[r-k][c])
	return max_arr

def main(file):
	ans = 0
	n_hidden = 0
	arr = []
	with open(file) as f:
		for l in f.readlines():
			l = l.strip().strip("\n")
			arr.append([int(i) for i in l])
	m = len(arr)
	n = len(arr[0])
	max_arrs = []
	# [l, r, t, b]
	s = [1, n-2, 1, m-2]
	e = [n-1, 0, m-1, 0]
	k = [1, -1, 1, -1]
	for i in range(4):
		_max_arr = calc_max_arr([a[:] for a in arr[:]], s[i], e[i], k[i], i<2)
		max_arrs.append(_max_arr)
	for r in range(1, m-1):
		for c in range(1, n-1):
			if (arr[r][c] <= max_arrs[0][r][c-1]) and (arr[r][c] <= max_arrs[1][r][c+1]) and (arr[r][c] <= max_arrs[2][r-1][c]) and (arr[r][c] <= max_arrs[3][r+1][c]):
				n_hidden += 1
	return m*n - n_hidden

file = sys.argv[1]
print(main(file))