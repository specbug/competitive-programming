def isMonotonic(array):
	a_type = None
	for i in range(len(array)):
		if i==len(array)-1:
			continue
		if array[i+1]>array[i] and a_type in [None, 'nd']:
			if a_type is None:
				a_type = 'nd'
		elif array[i+1]<array[i] and a_type in [None, 'ni']:
			if a_type is None:
				a_type = 'ni'
		elif (array[i+1]>array[i] and a_type=='ni') or \
				(array[i+1]<array[i] and a_type=='nd'):
			return False
	return True


array = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]
print(isMonotonic(array))