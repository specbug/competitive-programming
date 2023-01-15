class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ''
        for i in range(200):
            c = None
            for s in strs:
                if i >= len(s):
                    return ans
                if c is None:
                    c = s[i]
                else:
                    if s[i] != c:
                        return ans
            ans += c
        return ans
