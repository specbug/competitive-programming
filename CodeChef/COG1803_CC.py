t = int(input())
for _ in range(t):
	n = int(input())
	a = list(map(int, input().split()))
	a = sorted(a)
	a = [i for i in a if i != 0]
	y = sum(1 for i in a if i == 1)
	n = sum(1 for i in a if i == -1)
	if y>=n:
		print('YES')
	else:
		print('NO')