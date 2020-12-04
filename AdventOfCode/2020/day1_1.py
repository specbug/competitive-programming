def sum_2020(arr):
	total = 2020

	for i in arr:
		i_hat = total - i
		if i_hat in arr:
			return i*i_hat


with open('day1_ip.txt', 'r') as f:
	arr = [int(i) for i in f.read().strip().split('\n')]

print(sum_2020(arr))
