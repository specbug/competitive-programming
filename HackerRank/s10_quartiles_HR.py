def get_centroid(l):
	k = len(l)
	if k%2 != 0:
		return l[k//2]
	else:
		return (l[k//2-1] + l[k//2])//2

n = int(input())
l = list(map(int, input().split()))

l = sorted(l)
median = get_centroid(l)
q1 = get_centroid(l[:n//2])
if n%2!=0:
	q3 = get_centroid(l[n//2+1:])
else:
	q3 = get_centroid(l[n//2:])

print(str(q1)+'\n'+str(median)+'\n'+str(q3))