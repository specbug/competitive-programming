def fuel_req(i):
	if i < 7:
		return 0

	k = (i//3 - 2)
	
	return k + fuel_req(k)

	
f = open('day_1_input.txt', 'r')
print(sum([fuel_req(int(i.strip('\n'))) for i in f.readlines()]))


