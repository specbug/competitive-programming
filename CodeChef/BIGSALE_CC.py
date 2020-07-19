from decimal import *
pr = 0
ls = 0
t = int(input())
for i in range(t):
	n = int(input())
	count = 0
	for j in range(n):
		p, q, d = map(int, input().split())
		pr = Decimal(p+(p*d*Decimal(0.01)))
		ls = Decimal(pr-(pr*Decimal(d*0.01)))
		count+=Decimal((p-ls)*q)
	print(count)