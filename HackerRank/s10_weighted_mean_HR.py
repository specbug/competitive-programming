def weighted_mean(n, a, w):
	return round(sum([a[x]*w[x] for x in range(n)])/sum(w), 1)


n = int(input())
a = list(map(int, input().split()))
w = list(map(int, input().split()))

print(weighted_mean(n, a, w))