def std_fn(n, a):
	mean = sum(a)/n

	return round((sum([(i-mean)**2 for i in a])/n)**(1/2), 1)

n = int(input())
a = list(map(int, input().split()))

print(std_fn(n, a))

