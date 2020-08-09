def get_centroid(l):
	k = len(l)
	if k%2 != 0:
		return round(l[k//2]/1.0, 1)
	else:
		return round((l[k//2-1] + l[k//2])/2, 1)

n = int(input())
arr = list(map(int, input().split()))
f = list(map(int, input().split()))

l = [[arr[i]]*f[i] for i in range(n)]
l = [j for i in l for j in i]

l = sorted(l)
n = len(l)
q1 = get_centroid(l[:n//2])
if n%2!=0:
	q3 = get_centroid(l[n//2+1:])
else:
	q3 = get_centroid(l[n//2:])

print(q3-q1)