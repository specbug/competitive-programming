def n_invalid_passwords(arr):
	n = 0

	for i in arr:
		temp, password = i.split(': ')
		limit, key = temp.split()
		lower, upper = map(int, limit.split('-'))
		k_counter = 0

		for c in password:
			if c==key:
				k_counter+=1
			if k_counter>upper:
				k_counter = -1
				break

		if k_counter in range(lower, upper+1):
			n+=1

	return n

with open('day2_ip.txt', 'r') as f:
	arr = f.read().strip().split('\n')

print(n_invalid_passwords(arr))
