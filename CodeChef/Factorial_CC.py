t = int(input())

for _ in range(t):
	n = int(input())
	i = 5
	count = 0

	while (n/i) >= 1:
		count += int(n/i)
		i *= 5

	print(count)
