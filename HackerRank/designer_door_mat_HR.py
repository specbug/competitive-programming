n, m = map(int, input().split())
k = 1
r = 2

for i in range(1, n+1):
	if i == (n//2)+1:
		print('WELCOME'.center(m, '-'))
		r = -2
	else:
		print(str('.|.'*k).center(m, '-'))
	k += r