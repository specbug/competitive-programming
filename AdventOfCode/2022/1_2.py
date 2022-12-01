import sys

def n_calories(file):
	ans = [0]*3
	c_max = 0
	with open(file) as f:
		for l in f.readlines():
			if l.strip() == '':
				if c_max >= ans[0]:
					ans[1], ans[0] = ans[0], c_max
				elif c_max >= ans[1]:
					ans[2], ans[1] = ans[1], c_max
				elif c_max >= ans[2]:
					ans[2] = c_max
				c_max = 0
			else:
				c_max += int(l.strip())
	return sum(ans)


file = sys.argv[1]
print(n_calories(file))