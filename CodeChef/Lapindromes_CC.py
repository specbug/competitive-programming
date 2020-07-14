t = int(input())

for _ in range(t):
	s = str(input())
	half_s = int(len(s)/2)
	if len(s) % 2 == 0:
		if sorted(s[:half_s]) == sorted(s[half_s:]):
			print('YES')
		else:
			print('NO')

	else:
		if sorted(s[:half_s]) == sorted(s[(half_s+1):]):
			print('YES')
		else:
			print('NO')