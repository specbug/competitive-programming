class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ans = 0
        if len(s) == 1: return 1
        for i in range(len(s)-1, -1, -1):
            if s[i] == ' ' :
                if ans == 0:
                    continue
                break
            ans += 1
        return ans