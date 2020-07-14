t = int(input())

for _ in range(t):
	n = int(input())
	max_profit = 0
	for i in range(n):
		s, p, v = map(int, input().split())
		if ((p//(s+1))*v) >= max_profit:
			max_profit = ((p//(s+1))*v)

	print(max_profit)
