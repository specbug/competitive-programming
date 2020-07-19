t = int(input())
for i in range(t):
	n = int(input())
	val = 0
	k = 0
	l = [[0 for m in range(n)] for x in range(n)]
	count = [0]*n
	for j in range(n):
		l[j] = map(int, input().split())
		l[j] = [r for r in l[j] if r!=0]
		
	for j in range(n-1,-1,-1):
		if j==n-1:
			l[j].sort()
			count[k] = l[j][n-1]
			k+=1
		else:
			l[j].sort()
			try:
				for q in range(n-1,-1,-1):
					if l[j][q]>count[k-1]:
						l[j][q] = 0
				count[k] = max(l[j])
				k+=1
			except IndexError:
				val = 1
	if val==0:
		print(sum(count))
	else:
		print(-1)