t = int(input())
l = []
for i in range(1,t+1):
	flag = False
	power = 1  
	power1 = 1
	scnt = 0
	output = 0
	output1 = 0
	count = 0
	d, p = map(str, input().split())
	d = int(d)
	l = list(p)
	for j in l:
		if j=='S':
			output += power
			scnt+=1
		elif j=='C':
			power+=1
	print(output)
	if output<=d:
		print("Case #"+str(i)+":"+" "+str(0))
	elif scnt>d:
		print("Case #"+str(i)+":"+" "+"IMPOSSIBLE")
	else:
		for j1 in range(len(l)):
			if(l[j1]=='C' and j1!=len(l)-1):
				if(l[j1+1]=='S'):
					l[j1]='S'
					l[j1+1]='C'
					count+=1
				for j2 in l:
					if j2=='S':
						output1 += power1
					elif j2=='C':
						power1+=1
			if output1<=d:
				flag = True
				break
		if flag==False:
			print("Case #"+str(i)+":"+" "+"IMPOSSIBLE1")
		else:
			print("Case #"+str(i)+":"+" "+str(count))


