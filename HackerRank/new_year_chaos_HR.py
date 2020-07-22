def minimumBribes(q):
	swap_count = {}
	chaotic = False
	is_sorted = False

	while not is_sorted and not chaotic:
		for i in range(1, len(q)):
			if q[i] < q[i-1]:
				swap_count[q[i-1]] = swap_count.get(q[i-1], 0) + 1

				if swap_count[q[i-1]] > 2:
					chaotic = True
					break

				temp = q[i]
				q[i] = q[i-1]
				q[i-1] = temp

		if sorted(q) == q:
			is_sorted = True

	if not chaotic:
		print(sum(list(swap_count.values())))
	else:
		print('Too chaotic')


t = int(input())

for _ in range(t):
	n = int(input())
	q = list(map(int, input().rstrip().split()))
	minimumBribes(q)
