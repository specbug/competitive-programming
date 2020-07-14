t = int(input())

for _ in range(t):
	n = str(int(input()))
	print(int(''.join([i for i in n][::-1])))