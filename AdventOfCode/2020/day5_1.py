def partition(arr, key):
	n = len(arr)

	if len(arr)<2:
		return arr

	if key in ['L', 'F']:
		arr = arr[:n//2]
	else:
		arr = arr[n//2:]

	return arr

def max_seatID(arr):
	max_id = -1
	for i in arr:
		rows = list(range(0, 128))
		cols = list(range(0, 8))
		for c in i:
			if c in ['F', 'B']:
				rows = partition(rows, c)
			elif c in ['L', 'R']:
				cols = partition(cols, c)

		seat_id = rows[0] * 8 + cols[0]

		if seat_id > max_id:
			max_id = seat_id

	return max_id

with open('day5_ip.txt', 'r') as f:
	arr = f.read().strip().split('\n')

print(max_seatID(arr))