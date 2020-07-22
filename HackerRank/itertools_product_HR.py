import itertools

a = list(map(int, input().split()))
b = list(map(int, input().split()))

print(*itertools.product(a, b))