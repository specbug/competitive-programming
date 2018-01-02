def mutate(arr, k):
	arr_new = []
	m = 0
	for i in range(len(arr)):
		arr_new = arr[i]+k;
		if arr_new%7==0:
			m+=1
	return m

t = int(input())
n, k = map(int, input().split())
arr_in = list(map(int, input().split()))
print(mutate(arr_in, k))