class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        j = 0
        while i < len(chars) and j < len(chars):
            while chars[j] == chars[i]:
                j += 1
                if j >= len(chars):
                    break
            chars[i] = (chars[i], j-i)
            i = j
        chars[:] = [c for c in chars if isinstance(c, tuple)]
        chars[:] = [l for i in chars for j in i for l in str(j) if j != 1]
        return len(chars)