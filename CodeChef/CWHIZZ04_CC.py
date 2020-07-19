t = int(input())
for i in range(t):
	n = 0
	c = 0
	n = int(input())
	if n>0:
		while(n!=1):
			if n==2:
				n-=1
			elif n%3==0:
				n=int(n/3)
			elif (n+1)%3==0:
				n+=1
			elif (n-1)%3==0:
				n-=1
			c+=1
	elif n==0:
		c = 1

	print(c)