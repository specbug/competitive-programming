import sys


arr = []
countl = []
m=-1
for arr_i in range(6):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   arr.append(arr_t)

for k in range(4):
	for i in range(4):
		countl.append(int(arr[k][i])+int(arr[k][i+1])+int(arr[k][i+2])+int(arr[k+1][i+1])+int(arr[k+2][i])+int(arr[k+2][i+1])+int(arr[k+2][i+2]))

m = max(countl)
print(m)

