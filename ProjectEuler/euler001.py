def series(n, k):
	d = n//k
	return k * (d*(d+1)) // 2

t = int(input())

for _ in range(t):
	n = int(input())
	n = n-1
	print(series(n, 3) + series(n, 5) - series(n, 15))

