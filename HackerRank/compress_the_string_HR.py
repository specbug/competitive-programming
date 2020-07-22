import itertools

s = input()

print(*[(len(list(g)), int(k)) for k, g in itertools.groupby(s)])