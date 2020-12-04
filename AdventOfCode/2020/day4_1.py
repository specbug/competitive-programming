def n_valid_passports(arr):
	n = 0
	keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

	for i in arr:
		props = [j.split(':')[0] for j in i.strip().split()]
		if len(set(keys)-set(props))==0:
			n+=1

	return n



with open('day4_ip.txt', 'r') as f:
	arr = [i.replace('\n', ' ') for i in f.read().strip().split('\n\n')]

print(n_valid_passports(arr))