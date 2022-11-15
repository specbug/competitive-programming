def toh(d, n, s, t, i):
    if n == 1:
        print(f'Disk {d} moved from {s} to {t}')
        return
    toh(d-1, n-1, s, i, t)
    toh(d, 1, s, t, i)
    toh(d-1, n-1, i, t, s)

def tower_of_hanoi(n):
    ans = []
    toh(n, n, 'A', 'C', 'B')
    
n = int(input())
tower_of_hanoi(n)