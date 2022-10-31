"""
https://quastor.substack.com/p/facebook-interview-question-google
"""


def solve(A):
    if len(A) <= 2:
        return 0
    n = len(A)
    ml = A[0]
    mr = A[n - 1]
    i = 1
    j = n - 2
    ans = 0
    while i <= j:
        ml = max(ml, A[i])
        mr = max(mr, A[j])
        if ml <= mr:
            ans += ml - A[i]
            i += 1
        else:
            ans += mr - A[j]
            j -= 1
    return ans
