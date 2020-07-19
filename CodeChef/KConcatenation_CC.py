import sys

t = int(input().strip())
for i in range(t):
	a = []
	b = []
	m = 0
	maxn = 0
	count1 = 0
	n1 = 0
	n, k = map(int, input().strip().split())
	a = list(map(int, input().strip().split()))
	b = a*k
	c = [0]*len(b)
	j2 = 1
	for x in range(len(b)):
		if b[x]>0:
			count1+=1
	index = [0]*count1
	for j in range(len(b)):
		if b[j]>0:
			index[m] = j
			m+=1
	if sum(index)>0:
		for j1 in range(index[0],index[len(index)-1]+1,index[j2]):
			n1 = j1+1
			while n1<=(index[len(index)-1]+1):
				c = b[j1:n1]
				if sum(c)>maxn:
					maxn = sum(c)
				n1+=1
			j2+=1
	else:
		maxn = max(b)
	print(max(maxn,sum(b)))

