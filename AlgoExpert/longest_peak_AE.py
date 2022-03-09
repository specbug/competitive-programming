def peak_points(array, i, k):
	while True:
		if i-k<0 or i-k>len(array)-1:
			break
		if array[i]<=array[i-k]:
			break
		i -= k
	return i

def longestPeak(array):
	final = 0
	if len(array)<3:
		return final

	for i in range(len(array)):
		if i==0 or i==len(array)-1:
			continue
		if array[i-1]<array[i] and array[i]>array[i+1]:
			sp = peak_points(array, i, 1)
			ep = peak_points(array, i, -1)
			peak = ep-sp+1
			if final<peak:
				final=peak
	return final
				
array = [1, 2, 3, 3, 4, 0, 10]
print(longestPeak(array))