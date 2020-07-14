n = int(input())
l = []

for _ in range(n):
	l.append(int(input()))

l = sorted(l)
nl = list(reversed(range(1, len(l)+1)))

output = max([i*j for i,j in zip(l, nl)])

print(output)
