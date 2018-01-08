t = int(input())
for i in range(t):
    x, y, k, n = map(int, input().split())
    l = [0]*n
    cost = [1000]*n
    j=0
    for j in range(n):
    	l = list(map(int, input().split()))
    	if l[0]>=(x-y):
    		cost[j] = l[1]
    if min(cost)<=k:
    	print("LuckyChef")

    else:
    	print("UnluckyChef")
