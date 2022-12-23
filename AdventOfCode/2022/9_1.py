import sys

def shift(mod, h, t, x, y, k):
	h[x] += k
	if k > 0:
		a = h[x]
		b = t[x]
	else:
		a = t[x]
		b = h[x]
	if a - b > 1:
		t[x] += k
		if h[y] != t[y]:
			assert abs(t[y] - h[y]) < 2, f'H & T are too distant for {mod} shift.'
			t[y] = h[y]
	return h, t

def main(file):
	ans = 0
	h = [0, 0]
	t = [0, 0]
	pos_map = {
		'R': (0, 1, 1),
		'L': (0, 1, -1),
		'U': (1, 0, 1),
		'D': (1, 0, -1),
	}
	visited = set()
	visited.add(tuple(t))
	with open(file) as f:
		for l in f.readlines():
			l = l.strip().strip("\n")
			d, n = l.split()
			for i in range(int(n)):
				# print(d)
				h, t = shift(d, h, t, *pos_map[d])
				# print(h, t)
				visited.add(tuple(t))
	return len(visited)

file = sys.argv[1]
print(main(file))