t = int(input())
for i in range(t):
	n = int(input())
	s = str(input().strip())
	l = list(s)
	l = [x for x in l if x!="0"]
	print(int((len(l)*(len(l)+1))/2))
