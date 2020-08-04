def minion_game(string):
	vowels = ['A', 'E', 'I', 'O', 'U']
	n = len(string)
	kev = 0
	stu = 0

	for i in range(n):
		if string[i] in vowels:
			kev += n - i
		else:
			stu += n - i

	if stu > kev:
		print('Stuart', str(stu))
	elif kev > stu:
		print('Kevin', str(kev))
	else:
		print('Draw')

s = input()
minion_game(s)