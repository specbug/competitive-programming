def yes_meter(arr):
	n = 0
	for i in arr:
		n += len(set([c for c in i if c!='\n']))
	return n



with open('day6_ip.txt', 'r') as f:
	arr = f.read().strip().split('\n\n')

print(yes_meter(arr))