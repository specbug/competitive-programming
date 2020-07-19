def xor(l1=[], *args):
	c = int(l1[0])
	#print(l1)
	for j in range(1,len(l1)):
		c = c ^ l1[j]
	return(c)

l = 0
r = 0
count = []
n, k = map(int, input().split())
a = list(map(int, input().split()))
for i in range(int((n*(n+1))/2)):
	if r==n:
		l+=1
		r=l

	count.append(min(a[l:r+1])*xor(a[l:r+1]))
	r+=1

count.sort()
print(count[k-1])