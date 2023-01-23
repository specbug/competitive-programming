class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        freq = [0]*(n+1)
        for k, v in trust:
            freq[k] -= 1
            freq[v] += 1
        for i in range(1, n+1):
            if freq[i] == n-1:
                return i
        return -1
