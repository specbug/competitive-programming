import re

def n_valid_passports(arr):
	total = 0

	keys = {
	'byr': range(1920, 2003),
	'iyr': range(2010, 2021),
	'eyr': range(2020, 2031),
	'hgt': {'cm': range(150, 194), 'in': range(59, 77)},
	'hcl': r'^#[a-f0-9]{6}$',
	'ecl': ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
	'pid': r'^[0-9]{9}$'
	}

	present = list(keys.keys())

	for i in arr:
		props = [r.split(':')[0] for r in i.strip().split()]
		n = 0
		if len(set(present)-set(props))==0:
			for j in i.strip().split():
				k, v = j.split(':')
				k = k.strip()
				v = v.strip()
				if k in ['byr', 'iyr', 'eyr']:
					if int(v) in keys[k]:
						n += 1
				elif k in ['hcl', 'pid']:
					if re.match(keys[k], v) is not None:
						n += 1
				elif k == 'ecl':
					if v in keys[k]:
						n += 1
				elif k == 'hgt':
					if v.endswith('cm'):
						if int(v.rstrip('cm')) in keys[k]['cm']:
							n += 1
					elif v.endswith('in'):
						if int(v.rstrip('in')) in keys[k]['in']:
							n += 1
			if n==7:
				total += 1
	return total



with open('day4_ip.txt', 'r') as f:
	arr = [i.replace('\n', ' ') for i in f.read().strip().split('\n\n')]

print(n_valid_passports(arr))