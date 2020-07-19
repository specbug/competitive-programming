g = 0
l = []
c = 0
s1 = ""
s = str(input().strip())
q = int(input().strip())
for j in range(len(s)):
	for k in range(j, len(s)):
		l.append(s[j:k+1])
l.sort(key = str.lower)
for i1 in range(len(l)):
	s1 += l[i1]
for i in range(q):
	p, m = map(int, input().split())
	k = ((p*g)%m)+1
	g += ord(s1[k-1])
	print(s1[k-1])