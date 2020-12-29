def spiralTraverse(array):
	rows = len(array)
	cols = len(array[0])
	rs, re = 0, rows-1
	cs, ce = 0, cols-1
	results = []
	if rows==1:
		return array[0]
	if cols==1:
		return [i[0] for i in array]
	
	while rs<=re and cs<=ce:
		for col in range(cs, ce+1):
			results.append(array[rs][col])
		for row in range(rs+1, re+1):
			results.append(array[row][ce])
		for col in reversed(range(cs, ce)):
			if rs==re:
				break
			results.append(array[re][col])
		for row in reversed(range(rs+1, re)):
			if cs==ce:
				break
			results.append(array[row][cs])
			
		rs += 1
		cs += 1
		re -= 1
		ce -= 1

	return results
	
array = [[1], [3], [2], [5], [4], [7], [6]]
for r in range(len(array)):
	print(array[r])
print()
print(spiralTraverse(array))
