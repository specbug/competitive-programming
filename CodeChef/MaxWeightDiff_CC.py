t = int(input())
l = []
num1 = 0
num2 = 0
for i in range(t):
	n, k = map(int, input().split())
	l = list(map(int, input().split()))
	l.sort()
	num1 = sum(l[:k])
	num2 = sum(l[(n-k):n])
	print(max(abs(num1-(sum(l)-num1)), abs(num2-(sum(l)-num2))))