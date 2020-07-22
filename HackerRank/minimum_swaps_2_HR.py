def minimumSwaps(arr):
	index_map = dict(enumerate(arr))
	index_map = {v: k for k, v in index_map.items()}
	n_swaps = 0

	for i, v in enumerate(arr):
		if v != (i+1):
			arr[index_map[i+1]] = v
			arr[i] = (i+1)

			index_map[v] = index_map[i+1]
			index_map[i+1] = i

			n_swaps += 1

	return n_swaps

t = int(input())

for _ in range(t):
	n = int(input())
	arr = list(map(int, input().split()))
	print(minimumSwaps(arr))