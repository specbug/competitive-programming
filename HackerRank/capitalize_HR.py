def solve(s):
	return ' '.join([i[0].upper()+i[1:] if len(i)>1 else i[0].upper() if len(i)==1 else '' for i in s.split(' ')])

s = input()
result = solve(s)
print(result)