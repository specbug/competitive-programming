def shorten_search(sa, lv, n_flag):
	subarr = [i for i in sa if i<=lv]
	sa = list(set(sa) - set(subarr))
	if n_flag:
		final = [max(subarr), lv]
	else:
		final = [lv, max(subarr)]
	return sa, final

def binary_search(arr, val):
	n = len(arr)
	if n==2:
		return arr

	if val==arr[n//2]:
		return [val, val]
	elif val<arr[n//2]:
		return binary_search(arr[:n//2+1], val)
	else:
		return binary_search(arr[n//2:], val)

def get_min_pair(sa, la, final, min_v, n_flag):
	for i in sa:
		result = binary_search(la, i)
		if abs(result[0]-i) > abs(result[1]-i):
			if abs(result[1]-i) < min_v:
				if n_flag:
					final = [i, result[1]]
				else:
					final = [result[1], i]
				min_v = abs(result[1]-i)
		else:
			if abs(result[0]-i) < min_v:
				if n_flag:
					final = [i, result[0]]
				else:
					final = [result[0], i]
				min_v = abs(result[0]-i)
	return final

def smallestDifference(arrayOne, arrayTwo):
	arr1 = sorted(arrayOne)
	arr2 = sorted(arrayTwo)
	n_flag = False

	del arrayTwo, arrayOne
	
	if arr1[0]>arr2[0]:
		arr2, final = shorten_search(arr2, arr1[0], n_flag)
		if len(arr2)==0:
			return final
	else:
		n_flag = True
		arr1, final = shorten_search(arr1, arr2[0], n_flag)
		if len(arr1)==0:
			return final

	min_v = abs(final[0]-final[1])

	if n_flag:
		final = get_min_pair(arr1, arr2, final, min_v, n_flag)
	else:
		final = get_min_pair(arr2, arr1, final, min_v, n_flag)

	return final


arrayOne = [10, 0, 20, 25]
arrayTwo = [1005, 1006, 1014, 1032, 1031]

print(smallestDifference(arrayOne, arrayTwo))