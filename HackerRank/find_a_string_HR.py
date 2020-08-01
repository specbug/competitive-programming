def count_substring(string, sub_string):
	total_occ = 0
	lss = len(sub_string)
	for i in range(len(string)):
		if i+lss <= len(string):
			if sub_string == string[i:i+lss]:
				total_occ += 1

	return total_occ

string = input().strip()
sub_string = input().strip()

count = count_substring(string, sub_string)
print(count)