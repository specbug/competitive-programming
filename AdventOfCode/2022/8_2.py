import sys

def main(file):
	ans = 0
	arr = []
	with open(file) as f:
		for l in f.readlines():
			l = l.strip().strip("\n")
			arr.append([int(i) for i in l])
	m = len(arr)
	n = len(arr[0])
	for i in range(1, m-1):
		for j in range(1, n-1):
			u = i-1
			d = i+1
			l = j-1
			r = j+1
			while u > 0 and arr[u][j] < arr[i][j]:
				u -= 1
			while d < m-1 and arr[d][j] < arr[i][j]:
				d += 1
			while l > 0 and arr[i][l] < arr[i][j]:
				l -= 1
			while r < n-1 and arr[i][r] < arr[i][j]:
				r += 1
			ans = max(ans, (i-u)*(d-i)*(j-l)*(r-j))
	return ans

file = sys.argv[1]
print(main(file))