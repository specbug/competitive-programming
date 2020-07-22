n = int(input())
arr = map(int, input().split())

print(sorted(list(set(arr)), reverse=True)[1])