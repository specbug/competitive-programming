class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        smap = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
        c = 0
        for i in range(k):
            if s[i] in smap:
                smap[s[i]] = smap.get(s[i], 0) + 1
                c += 1
        ans = c
        for i in range(len(s)-k):
            if s[i] in smap:
                c -= 1
            if s[i+k] in smap:
                c += 1
            ans = max(ans, c)
        return ans

