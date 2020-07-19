n = int(input())
h = [0]
ans = 0
for _ in range(n):
	temp_p, temp_h = map(int, input().split())
	for i in range(temp_h):
		ans += (10 * temp_p)
		h.append(10 * temp_p)
q = int(input())
for _ in range(q):
	ans1 = ans
	l, r = map(int, input().split())
	for i in range(l+1):
		ans1 -= h[i]
	for i in range(r+1,len(h)):
		ans1 -= h[i]
	print(ans1)
