class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        if len(s) != len(pattern):
            return False
        pattern_map = dict()
        str_map = dict()
        for i, c in enumerate(pattern):
            if c in pattern_map or s[i] in str_map:
                if c in pattern_map and pattern_map[c] != s[i]:
                    return False
                elif s[i] in str_map and str_map[s[i]] != c:
                    return False
            else:
                pattern_map[c] = s[i]
                str_map[s[i]] = c
        return True