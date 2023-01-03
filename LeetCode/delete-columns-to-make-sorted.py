class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        ans = set()
        n = len(strs)
        m = len(strs[0])
        for i in range(1, n):
            for j in range(m):
                if j in ans:
                    continue
                if strs[i][j] < strs[i-1][j]:
                    ans.add(j)
                    continue
        return len(ans)