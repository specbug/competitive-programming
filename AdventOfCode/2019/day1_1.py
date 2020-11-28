def fuel_req(l_module_mass):
	return sum([(int(i.strip('\n'))//3 - 2) for i in l_module_mass])


f = open('day_1_input.txt', 'r')
print(fuel_req(f.readlines()))


