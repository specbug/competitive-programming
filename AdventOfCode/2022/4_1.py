import sys

def main(file):
	ans = 0
	with open(file) as f:
		for l in f.readlines():
			a, b = l.strip().strip('\n').split(',')
			a = tuple(map(int, a.split('-')))
			b = tuple(map(int, b.split('-')))
			if (a[0] <= b[0] and a[1] >= b[1]) or (b[0] <= a[0] and b[1] >= a[1]):
				ans += 1
	return ans


file = sys.argv[1]
print(main(file))
