class Solution:
    def reverse(self, s, start, end):
        n = len(s)
        for i in range((end-start+1)//2):
            s[start+i], s[-1-(n-end-1)-i] = s[-1-(n-end-1)-i], s[start+i]
        return s
    
    def reverseWords(self, s: str) -> str:
        s = list(s)
        st, ed = -1, -1
        for i in range(len(s)):
            if st == -1 and s[i] != ' ':
                st = i
            if ed == -1 and s[-1-i] != ' ':
                ed = len(s)-1-i
            if i > 0:
                if s[i] == ' ' and s[i-1] == ' ':
                    s[i-1] = None
        s = s[st:ed+1]
        s = [c for c in s if c is not None]
        n = len(s)
        if n < 3:
            return ''.join(s)
        s = self.reverse(s, 0, n-1)
        start = 0
        for end in range(n):
            if s[end] == ' ':
                s = self.reverse(s, start, end-1)
                start = end + 1
        if start < n-1:
            s = self.reverse(s, start, n-1)
        return ''.join(s)