def sum_2020(arr, total):

	for i in range(len(arr)):
		i_hat = total - arr[i]
		if total == 2020:
			sub_com = sum_2020(arr[i+1:], i_hat)
			if sub_com is not None:
				return arr[i]*sub_com
		else:
			if i_hat in arr:
				return arr[i]*i_hat

	return None


with open('day1_ip.txt', 'r') as f:
	arr = [int(i) for i in f.read().strip().split('\n')]

print(sum_2020(arr, 2020))