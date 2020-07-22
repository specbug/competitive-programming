memo = {2: 2, 5: 8}

def even_fibonacci(n):
	global memo

	if n not in memo:
		memo[n] = 4*even_fibonacci(n-3) + even_fibonacci(n-6)

	return memo[n]

t = int(input())

for _ in range(t):
	n = int(input())

	total = 0

	k = 0
	i = 2
	while True:
		k = even_fibonacci(i)
		if k > n:
			break
		total += k
		i += 3

	print(total)