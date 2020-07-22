def arrayManipulation(n, queries):
	l = [0]*(n+1)
	m = len(queries)
	max_n = -1
	s = 0

	for q in range(m):
		a, b, k = queries[q]
		l[a] += k
		if b < n:
			l[b+1] -= k

	for i in l:
		s += i
		if s > max_n:
			max_n = s

	return max_n

n, m = map(int, input().split())
queries = []

for _ in range(m):
	queries.append(list(map(int, input().split())))

print(arrayManipulation(n, queries))