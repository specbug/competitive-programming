def xore(a, p ,q, l):
	j=0
	max=-1
	m = []
	for i in range(p-1,q):
		m.append(int(l[i]) ^ a)
		if int(m[j])>max:
			max=m[j]
		j+=1
	return max

t = input()
l = []
m = []
for i in t:
	n, x = map(int, input().split())
	l = list(map(str, input().split()))
	for k in range(x):
		a, p, q = map(int, input().split())
		out=xore(a, p, q, l)
		print(out)
