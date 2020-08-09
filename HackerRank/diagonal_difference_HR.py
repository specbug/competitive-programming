def diagonalDifference(arr):
	n = len(arr)-1
	if n%2 == 0:
		k = len(arr)//2+1
	else:
		k = len(arr)//2
	d1 = 0
	d2 = 0
	for i in range(k):
		d1 = d1 + arr[i][i] + arr[n-i][n-i] 
		d2 = d2 + arr[i][n-i] + arr[n-i][i]

	return abs(d1 - d2)

n = int(input().strip())

arr = []

for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))

result = diagonalDifference(arr)
print(result)