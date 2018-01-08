t = int(input())
for i in range(t):
	n = int(input())
	a = [1]*n
	k = n-1
	l = list(map(int, input().split()))
	for i in range(n-1,0,-1):
		if l[i]/abs(l[i]) != l[i-1]/abs(l[i-1]) and l[i]!=0 and l[i-1]!=0:
			a[i-1] = a[i]+1
		elif l[i]==0:
			if l[i]>l[i-1]:
				a[i-1] = a[i]+1
		elif l[i-1]==0:
			if l[i]<l[i-1]:
				a[i-1] = a[i]+1

	for j in a:
		print(j, end=" ")
	if i!=t-1:	
		print()