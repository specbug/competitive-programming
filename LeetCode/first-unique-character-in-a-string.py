class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq_map = [0] * 26
        ascii_offset = 97
        for c in s:
            freq_map[ord(c) - ascii_offset] += 1
        for e, c in enumerate(s):
            if freq_map[ord(c) - ascii_offset] == 1:
                return e
        return -1