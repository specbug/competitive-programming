import sys

max1 = int(-1)
n = int(input().strip())
bi = "{0:b}".format(n)
#print(bi)
counts = []
counts = bi.split('0')
for i in counts:
	if(len(i)>max1):
		max1=len(i);
print(max1)
