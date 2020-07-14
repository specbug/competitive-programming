def countingValleys(n, s):
	
	net_topology = 0
	valley_flag = False
	n_valleys = 0
	d = {'U':1, 'D':-1}

	for i in s:
		
		net_topology += d[i]

		if not valley_flag and net_topology == -1:
			n_valleys += 1
			valley_flag = True
		if valley_flag and net_topology >= 0:
			valley_flag = False

	return n_valleys


s = [i for i in 'UDDDUDUU']
print(s)
print(countingValleys(len(s), s))


