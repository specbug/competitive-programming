def n_invalid_passwords(arr):
	n = 0

	for i in arr:
		temp, password = i.split(': ')
		limit, key = temp.split()
		first, sec = map(int, limit.split('-'))
		first -= 1
		sec -= 1

		if first<len(password) and sec<len(password):
			if password[first]==key:
				if password[sec]==key:
					continue
				n+=1
			elif password[sec]==key:
				n+=1

	return n

with open('day2_ip.txt', 'r') as f:
	arr = f.read().strip().split('\n')

print(n_invalid_passwords(arr))
