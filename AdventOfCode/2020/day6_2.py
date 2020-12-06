def yes_meter(arr):
	n = 0
	for i in arr:
		this_g = set()
		first = True
		for j in i.split('\n'):
			if len(this_g)==0:
				if first:
					this_g = set([c for c in j.strip()])
					first = False
				else:
					break
			else:
				this_g = this_g & set([c for c in j.strip()])

		n += len(this_g)
	return n



with open('day6_ip.txt', 'r') as f:
	arr = f.read().strip().split('\n\n')

print(yes_meter(arr))