class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans = ''
        m = len(a)
        n = len(b)
        l = max(m, n)
        a = '0'*(l-m) + a
        b = '0'*(l-n) + b
        c = 0
        imap = {'1': 1, '0': 0}
        for i in range(l-1, -1, -1):
            val = imap[a[i]] + imap[b[i]] + c
            c = 0
            c = int(val>=2)
            if val >= 3:
                ans += '1'
            else:
                ans += str(val&1)
        while c != 0:
            ans += '1'
            c -= 1
        return ans[::-1]
