import itertools

s, k = input().split()

print(*sorted([''.join(list(i)) for i in list(itertools.permutations(s, int(k)))]), sep='\n')