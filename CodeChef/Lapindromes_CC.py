t = int(input())
ls = []
rs = []
s = []
for i in range(t):
	s = list(input())
	mid = int(len(s)/2)
	if len(s)%2==0:
		ls = s[0:mid]
		rs = s[mid:]
	else:
		del s[mid]
		ls = s[0:mid]
		rs = s[mid:]
	if(sorted(ls) == sorted(rs)):
		print("YES")
	else:
		print("NO")