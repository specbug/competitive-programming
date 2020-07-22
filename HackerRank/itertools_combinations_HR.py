import itertools

s, k = input().split()
s = sorted(s)
k = int(k)

l = []
for r in range(1, k+1):
    l += [''.join(list(i)) for i in list(itertools.combinations(s, r))]

print(*l, sep='\n')
