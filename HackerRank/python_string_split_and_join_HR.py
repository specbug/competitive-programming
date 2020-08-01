def split_and_join(line):
	return '-'.join(line.split(' '))

s = input().rstrip()
print(split_and_join(s))