def swap_case(s):
	return ''.join([c.upper() if c==c.lower() else c.lower() for c in s])

s = input().rstrip()
print(swap_case(s))