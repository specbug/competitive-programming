import sys

def n_calories(file):
	ans = 0
	c_max = 0
	with open(file) as f:
		for l in f.readlines():
			if l.strip() == '':
				ans = max(ans, c_max)
				c_max = 0
			else:
				c_max += int(l.strip())
	return ans


file = sys.argv[1]
print(n_calories(file))