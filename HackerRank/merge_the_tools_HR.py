def merge_the_tools(s, k):
	n = len(s)//k
	n_s = 0
	n_e = k
	for _ in range(n):
		l = []
		t = s[n_s:n_e]
		for c in t:
			if c not in l:
				l.append(c)
		print(''.join(l))

		n_s += k
		n_e += k

s, k = input(), int(input())
merge_the_tools(s, k)