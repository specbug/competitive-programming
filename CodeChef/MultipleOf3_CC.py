t = int(input())

for _ in range(t):
    k, d0, d1 = map(int, input().split(' '))
    a = [d0, d1, (d0 + d1) % 10]

    s = sum(a[:k])

    if k > 3:
        b = [(a[-1]*(2**i)) % 10 for i in range(1, 5)]
        d, r = divmod(k - 3, 4)
        s += ((sum(b) * d) + sum(b[:r]))

    print("YES") if s%3==0 else print("NO")
