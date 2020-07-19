k = []
b = {}
an = ""
max1 = 0
n = int(input().strip())
for i in range(n):
	l = list(map(str, input().strip().split()))
	b.update({l[x]:(int(l[x+2])-int(l[x+1])) for x in range(0, len(l), 3)})
for w in sorted(b, key=b.get, reverse=True):
	an = w
	max1 = b[w]
	break
print(an, end=" ")
print(max1)