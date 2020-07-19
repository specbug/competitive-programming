t = int(input())
for _ in range(t):
	s = str(input().strip())
	if "not" in s.split():
		print('Real Fancy')
	else:
		print('regularly fancy')