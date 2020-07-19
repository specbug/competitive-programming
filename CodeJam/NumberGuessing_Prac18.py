t = int(input())
for i in range(t):
	count = 0
	g = 0
	s = ""
	a,b = map(int, input().split())
	a+=1
	n = int(input())
	while s!="CORRECT":
		g = int((a+b)/2)
		print(g)
		s = str(input())
		if a==g and s!="CORRECT":
			g=b
		elif b==g and s!="CORRECT":
			g=a
		if s=="TOO_BIG":
			b=g
		elif s=="TOO_SMALL":
			a=g
		elif s=="WRONG_ANSWER":
			break			