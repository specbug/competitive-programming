def descriptive_stats(a, n):
    print(round(sum(a)/n, 1))

    a = sorted(a)

    if n%2 == 0:
        print(round(float((a[int(n/2)-1] + a[int(n/2)])/2), 1))
    else:
        print(round(float(a[n//2]), 1))

    f_a = {}
    max_k = 0
    max_v = -1

    for i in a:
        f_a[i] = f_a.get(i, 0) + 1

    for j in list(set(a)):
        if f_a[j] >= max_v:
            if f_a[j] == max_v:
                max_k = min(max_k, j)
            else:
                max_k = j
                max_v = f_a[j]

    print(max_k)

n = int(input())
a = list(map(int, input().split()))

descriptive_stats(a, n)