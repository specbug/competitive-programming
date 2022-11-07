"""
https://quastor.substack.com/p/-netflix-ceo-smacks-down-work-from
"""

def firstUniqChar(s: str) -> int:
    freq_map = [0] * 26
    ascii_offset = 97
    for c in s:
        freq_map[ord(c) - ascii_offset] += 1
    for e, c in enumerate(s):
        if freq_map[ord(c) - ascii_offset] == 1:
            return e
    return -1


tc1 = "leetcode"
tc2 = "loveleetcode"
tc3 = "aabb"

print(firstUniqChar(tc1) == 0)
print(firstUniqChar(tc2) == 2)
print(firstUniqChar(tc3) == -1)