dic = {}
t = int(input())
for i in range(t):
	k, v = input().split()
	dic[k] = v

while True:
	name = str(input())
	if name in dic:
		print(name+'='+dic[name])
	else:
		print('Not found')
