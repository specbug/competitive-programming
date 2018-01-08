t = int(input())
l = []
for i in range(t):
	n, c = map(int, input().split())
	l = list(map(int, input().split()))
	if sum(l)>c:
		print("No")
	else:
		print("Yes")