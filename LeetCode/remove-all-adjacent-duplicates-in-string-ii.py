class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        ans = []
        for i in s:
            if len(ans) == 0:
                ans.append([i, 1])
                continue
            if i == ans[-1][0]:
                ans[-1][1] += 1
                if ans[-1][1] == k:
                    ans.pop()
            else:
                ans.append([i, 1])
        return ''.join([c*n for c, n in ans])
