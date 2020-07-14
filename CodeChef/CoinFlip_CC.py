t = int(input())

for _ in range(t):
	games = int(input())
	for g in range(1, games+1):
		i, n, q = map(int, input().split())

		if i == q:
			print(n//2)
		else:
			print(n - (n//2))

