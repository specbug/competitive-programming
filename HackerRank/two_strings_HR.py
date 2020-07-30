def twoStrings(s1, s2):
	if len(set([i for i in s1]) & set([j for j in s2])) > 0:
		return 'YES'
	return 'NO'

t = int(input())

for _ in range(t):
	s1 = input().rstrip()
	s2 = input().rstrip()
	print(twoStrings(s1, s2))