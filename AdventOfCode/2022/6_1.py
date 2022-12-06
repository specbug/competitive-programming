import re
import sys

def main(file):
	ans = -1
	wstart = 0
	wend = 0
	with open(file) as f:
		for l in f.readlines():
			l = l.strip().strip('\n')
			for e, c in enumerate(l):
				wend = e
				if (wend-wstart+1) < 4:
					continue
				if len(set(l[wstart:wend+1])) == 4:
					return wend+1
				else:
					wstart += 1
	return ans


file = sys.argv[1]
print(main(file))