class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m = len(s1)
        n = len(s2)
        if n < m:
            return False
        smap = dict()
        t = 0
        for i in s1:
            smap[i] = smap.get(i, 0) + 1
            t += 1
        hmap = dict()
        c = 0
        for i in range(m):
            x = s2[i]
            if x not in smap:
                continue
            hmap[x] = hmap.get(x, 0) + 1
            if hmap[x] <= smap[x]:
                c += 1
            if c == t:
                return True
        for i in range(n-m):
            x = s2[i]
            y = s2[i+m]
            if x in smap:
                hmap[x] = max(0, hmap.get(x, 0) - 1)
                if hmap[x] < smap[x]:
                    c -= 1
            if y in smap:
                hmap[y] = hmap.get(y, 0) + 1
                if hmap[y] <= smap[y]:
                    c += 1
            if c == t:
                return True
        return False
