t = int(input())
for c in range(t):
	l = []
	n, m = map(int, input().split())
	a = [[[0 for k in range(n)] for j in range(n)] for i in range(n)]
	for c1 in range(m):
		flag = 0
		s = 0
		l = list(map(str, input().split()))
		if l[0] == "UPDATE":
			a[int(l[1])-1][int(l[2])-1][int(l[3])-1] = int(l[4])
		elif l[0] == "QUERY":
			for i1 in range(int(l[1]),n+1):
				for j1 in range(1, n+1):
					for k1 in range(1, n+1):
						if i1 == int(l[4]):
							if j1 == int(l[5]):
								if k1 == int(l[6])+1:
									i1 = j1 = k1 = n+2									
									flag = 1

						if flag==0:
							s += a[i1-1][j1-1][k1-1]
			print(s)
