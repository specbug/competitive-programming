def gcd(a, b):
	temp = 1
	while(b!=0):
		temp = a%b
		a = b
		b = temp
	return a

t = int(input())
for _ in range(t):
	n, a, b, k = map(int, input().split())
	gcd_ab = gcd(a, b) 
	gcd_a = int(a / gcd_ab)
	temp_a = int(gcd_a * b)
	optimal = ((int(n/a)) + (int(n/b))) - (2*(int(n/(temp_a))))
	if a==b:
		optimal = 0
	if optimal >= k:
		print('Win')
	else:
		print('Lose')
