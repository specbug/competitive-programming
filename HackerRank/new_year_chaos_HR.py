def minimumBribes(q):


t = int(input())

for _ in range(t):
	n = int(input())
	q = list(map(int, input().rstrip().split()))
	print(minimumBribes(q))
	