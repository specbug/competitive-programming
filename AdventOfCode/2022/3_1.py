import sys

def main(file):
	ord_map = {(chr(k+96) if k <= 26 else chr(k-26+64)):k for k in range(1, 53)}
	ans = 0
	with open(file) as f:
		a = set()
		b = set()
		for l in f.readlines():
			a = set(l[:len(l)//2])
			b = set(l[len(l)//2:])
			ans += ord_map[next(iter(a & b))]
	return ans


file = sys.argv[1]
print(main(file))
