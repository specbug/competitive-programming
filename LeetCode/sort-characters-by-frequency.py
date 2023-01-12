class Solution:
    def frequencySort(self, s: str) -> str:
        freq = dict()
        for c in s:
            freq[c] = freq.get(c, 0) + 1
        freq = dict(sorted(freq.items(), key=lambda i: i[1], reverse=True))
        return ''.join([k*v for k, v in freq.items()])