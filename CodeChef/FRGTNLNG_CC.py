t=int(input())
for i in range(t):
	n,m=map(int,input().split())
	l=[x for x in input().split()]
	p=[]
	for j in range(m):
		x=[y for y in input().split()]
		p.append(x[1:])
	q=[]
	for j in l:
		flag=False
		for k in range(len(p)):
			if(j in p[k]):
				q.append("YES")
				flag=True
				break
		if(flag==False):
			q.append("NO")
	print(" ".join(q)) 