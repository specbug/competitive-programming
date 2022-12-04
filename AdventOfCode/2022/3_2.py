import sys

def main(file):
	ord_map = {(chr(k+96) if k <= 26 else chr(k-26+64)):k for k in range(1, 53)}
	ans = 0
	with open(file) as f:
		a = set()
		b = set()
		c = 1
		common = None
		for l in f.readlines():
			l = l.strip().strip('\n')
			if c < 3:
				if not common:
					common = set(l)
				else:
					common = common & set(l)
				c += 1
			elif c == 3:
				common = common & set(l)
				ans += ord_map[next(iter(common))]
				c = 1
				common = None
	return ans

file = sys.argv[1]
print(main(file))