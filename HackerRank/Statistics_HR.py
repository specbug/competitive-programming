from scipy.stats import mode

n = int(input())
x = list(map(int, input().split()))
mean = 0
for i in range(n):
	mean+=x[i]
mean/=n
max=-1
counts = []
x.sort()
if n%2!=0:
	median = x[int(n/2)]
else:
	median = (x[int(n/2)]+x[int((n+1)/2)])/2
count = 0
first = second = float('-inf')
for j in x:
	count+=1
	if j > second:
		if j>=first:
			first,second = j, first
		else:
			second = j
if count >= 2:
	modes = second
print(mean)
print(median)
print(modes)