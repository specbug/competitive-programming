N = int(input())
l = []

for _ in range(N):
    line = input().split()
    op = line[0]
    if len(line) > 1:
        line[1] = int(line[1])
    if op == 'insert':
        l.insert(line[1], int(line[2]))
    elif op == 'append':
        l.append(line[1])
    elif op == 'remove':
        l.remove(line[1])
    elif op == 'pop':
        l.pop()
    elif op == 'reverse':
        l.reverse()
    elif op == 'sort':
        l.sort()
    elif op == 'print':
        print(l)
