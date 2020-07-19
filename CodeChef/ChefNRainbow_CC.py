l = []
r = []
flag = 0
t = int(input())
for i in range(t):
	n = int(input())
	a = list(map(int, input().split()))
	indx = [0]*(n-12)
	if len(a)<13:
		flag = 1
	elif len(a)>=13:
		s = set(a)
		s1 = list(s)
		if sum(s1)==28 and len(s1)==7:
			for i1 in range(len(s1)):
				if i1!=0:
					if s1[i1]!=(s1[i1-1]+1):
						flag = 1
					else:
						flag = 0
		else:
			flag = 1
		if flag == 0:
			if len(a)%2==0:
				l = a[:int(len(a)/2)]
				r = a[int(len(a)/2):]
				if l!=r[::-1]:
					flag = 1
			else:
				for j in range(len(a)):
					if a[j]==7:
						indx.append(j)
				indx = [x for x in indx if x!=0]
				for j1 in range(indx[0]):
					l.append(a[j1])
				for j1 in range(indx[len(indx)-1]+1,len(a)):
					r.append(a[j1])
				if l!=r[::-1] or (len(indx)%2==0 and len(indx)>1):
					flag = 1
	if flag==0:
		print("yes")
	elif flag == 1:
		print("no")
