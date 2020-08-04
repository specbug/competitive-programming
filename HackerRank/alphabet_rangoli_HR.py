def print_rangoli(size):
	w = (2 * (size*2-1) - 1)
	al = [chr(96+i) for i in range(1, size+1)]
	c = -1

	for i in range(1, 2*size):
		sub = al[c:]
		print('-'.join(sub[-1:-len(sub):-1] + sub).center(w, '-'))
		if i >= size:
			c += 1
		else:
			c -= 1

n = int(input())
print_rangoli(n)