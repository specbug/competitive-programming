def jumpingOnClouds(c):
	n_jumps = 0

	i = 0
	while i < len(c)-1:
		if (i < len(c)-2) and (c[i+2] == 0):
			i += 2
		else:
			i += 1

		n_jumps += 1

	return n_jumps

c = '0100010'
c = [int(i) for i in c]
print(jumpingOnClouds(c))