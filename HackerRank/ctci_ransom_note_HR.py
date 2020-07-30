def checkMagazine(magazine, note):
	mag_c = {}
	note_c = {}
	sat = True

	for i in magazine:
		mag_c[i] = mag_c.get(i, 0) + 1
	
	for j in note:
		note_c[j] = note_c.get(j, 0) + 1

		if mag_c.get(j, 0) < note_c[j]:
			sat = False
			break

	if sat:
		print('Yes')
	else:
		print('No')
		

m, n = map(int, input().split())
magazine = input().split()
note = input().split()

checkMagazine(magazine, note)