t = int(input())
for _ in range(t):
	n = int(input())
	a = list(map(int, input().split()))
	d = list(map(int, input().split()))
	max_d = -1
	for i in range(n):
		if i == 0:
			if (a[-1] + a[i+1]) < d[i]:
				if d[i] > max_d:
					max_d =  d[i]
		elif i == n-1:
			if (a[i-1]+a[0]) < d[i]:
				if d[i] > max_d:
					max_d = d[i]
		else:
			if (a[i-1] + a[i+1]) < d[i]:
				if d[i] > max_d:
					max_d = d[i]
	print(max_d)