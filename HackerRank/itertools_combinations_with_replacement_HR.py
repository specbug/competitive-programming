import itertools

s, k = input().split()
s = sorted(s)
k = int(k)


print(*[''.join(list(i)) for i in itertools.combinations_with_replacement(s, k)], sep='\n')
