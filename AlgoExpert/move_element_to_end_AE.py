def moveElementToEnd(array, toMove):
	p1 = 0
	p2 = len(array)-1
	
	if len(array)==0:
		return []

	while p1<p2:
		if array[p1]==toMove and array[p2]!=toMove:
			temp = array[p1]
			array[p1] = array[p2]
			array[p2] = temp
		else:
			if array[p1]!=toMove:
				p1 += 1
			if array[p2]==toMove:
				p2 -= 1
				
	return array

array = [2, 1, 2, 2, 2, 3, 4, 2]
toMove = 2

print(moveElementToEnd(array, toMove))