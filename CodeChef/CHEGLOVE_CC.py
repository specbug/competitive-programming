t = int(input())
for i in range(t):
	fr = 0
	bk = 0
	n = int(input())
	f = list(map(int, input().split()))
	g = list(map(int, input().split()))
	for j in range(len(f)):
		if(f[j]-g[j]>0):
			fr = 1
	rf = list(reversed(f))
	for j1 in range(len(rf)):
		if(rf[j1]-g[j1]>0):
			bk = 1
	if(fr==0):
		if(bk==0):
			print("both")
		else:
			print("front")
	elif(bk==0):
		print("back")
	else:
		print("none")