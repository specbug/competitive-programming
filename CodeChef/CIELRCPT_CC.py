import math
t = int(input())
for i in range(t):
	n = int(input())
	count = 0
	flag = False
	while(flag==False):
		if n>2048:
			count+=1
			n-=2048
		if n-pow(2, int(math.log2(n)))>=0:
			n-=pow(2, int(math.log2(n)))
			count+=1
			if n==0:
				flag=True
			if n==1:
				count+=1
				flag=True
	print(count)

