def partition(arr, key):
	n = len(arr)
	if len(arr)<2:
		return arr
	if key in ['L', 'F']:
		arr = arr[:n//2]
	else:
		arr = arr[n//2:]
	return arr

def find_seat(arr):
	all_ids = []
	for i in arr:
		rows = list(range(0, 128))
		cols = list(range(0, 8))
		for c in i:
			if c in ['F', 'B']:
				rows = partition(rows, c)
			elif c in ['L', 'R']:
				cols = partition(cols, c)

		seat_id = rows[0] * 8 + cols[0]
		all_ids.append(seat_id)

	all_ids = sorted(all_ids)

	for i in range(len(all_ids)):
		if i < len(all_ids)-1:
			if all_ids[i+1] - all_ids[i] == 2:
				return all_ids[i]+1

with open('day5_ip.txt', 'r') as f:
	arr = f.read().strip().split('\n')

print(find_seat(arr))