def rotLeft(a, d):
	
	if d%len(a) == 0:
		return a
	elif d > len(a):
		n_rot = len(a)-(len(a)*(d//len(a)))
	else:
		n_rot = d
	return a[n_rot:] + a[:n_rot]

a = [1, 2, 3, 4, 5]
d = 4

print(rotLeft(a, d))
