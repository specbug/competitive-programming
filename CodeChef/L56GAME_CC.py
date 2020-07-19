l = []
r = []
index = 0
t = int(input())
for i in range(t):
	n = int(input())
	l = list(map(int, input().split()))
	l=[x for x in l if x%2==0]
	r=[x for x in l if x%2!=0]
	print(a)