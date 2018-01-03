t = int(input())
l = []
num1 = num2 = 0
for i in range(t):
	n, k = map(int, input().split())
	l = list(map(int, input().split()))
	l.sort()
	num1 = sum(l[:k])
	num2 = sum(l[k:])
	print(num2-num1)