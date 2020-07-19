t = int(input())
for _ in range(t):
	n = int(input())
	s = []
	ts = ''
	for i in range(n):
		s.append(''.join(sorted(set(str(input())))))
	match_str = min(s, key=len)
	final_s = ''.join(x.strip() for x in s)
	d = {}
	c = 0
	for i in final_s:
		if i in match_str:
			d[i] = d.get(i, 0) + 1
	for j in d:
		if d[j] >= len(s):
			c += 1
	print(c)