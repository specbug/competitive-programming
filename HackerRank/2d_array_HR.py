import math

def hourglassSum(arr):

	n = len(arr)
	f = 3
	op_shape = n-f+1
	max_v = -math.inf

	filter_mat = [[1,1,1], [0,1,0], [1,1,1]]

	for h in range(op_shape):
		vert_start = h
		vert_end = vert_start + f
		for w in range(op_shape):
			horiz_start = w
			horiz_end = horiz_start + f

			arr_slice = [arr[row][horiz_start:horiz_end] for row in range(vert_start, vert_end)]
			
			k = sum([sum([arr_slice[i][j] * filter_mat[i][j] for j in range(len(arr_slice[i]))]) for i in range(len(arr_slice))])

			if k > max_v:
				max_v = k

	return max_v

arr = [[0,-4,-6,0,-7,-6], [-1,-2,-6,-8,-3,-1], [-8,-4,-2,-8,0,0], [0,0,2,4,4,0], [0,0,0,2,0,0], [0,0,1,2,4,0]]

print(hourglassSum(arr))
