import math
import operator as op
from functools import reduce

def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer//denom

try:
	t = int(input())
	for _ in range(t):
		n, p, k = map(int, input().split())
		a = list(map(int, input().split()))
		ans = 0
		temp = 0
		sorted(a)
		flag = True
		s = a[:]
		a = list(set(a))
		largest = max(a)
		x = float(largest)/p
		x = int(math.ceil(x))
		min_index = len(a) - 1 - a[::-1].index(x)
		list_of_max = len(a[min_index:])
		ans += ncr(list_of_max, k)
		if min_index != 0:
			for i in reversed(range(min_index)):
				ans += ncr(((a[i]*p)-a[i]+1), k)
				ans -= ncr(((a[i]*p)-a[i]), k)
		ans += len(set([x for x in s if s.count(x) > 1]))
		mod = 1000000007
		ans = ans%mod
		print(ans)
except Exception as e:
	print(e)