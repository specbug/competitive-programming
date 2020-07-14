t = int(input())

for _ in range(t):
	n = int(input())
	v = list(map(int, input().split()))

	n_cars = 1

	if len(v) == 1:
		print(n_cars)
		continue

	for i in range(1, len(v)):

		if v[i-1] >= v[i]:
			n_cars += 1
		else:
			v[i] = v[i-1]

	print(n_cars)