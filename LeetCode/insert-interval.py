class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        ans = []
        for i in range(len(intervals)):
            nxt = intervals[i]
            if newInterval and newInterval[0] <= nxt[0]:
                if ans and newInterval[0] <= ans[-1][1]:
                    prev = ans.pop()
                    ans.append([min(prev[0], newInterval[0]), max(prev[1], newInterval[1])])
                else:
                    ans.append(newInterval)
                newInterval = None
            if ans and nxt[0] <= ans[-1][1]:
                prev = ans.pop()
                ans.append([min(prev[0], nxt[0]), max(prev[1], nxt[1])])
            else:
                ans.append(nxt)
        if newInterval:
            if newInterval[0] <= ans[-1][1]:
                prev = ans.pop()
                ans.append([min(prev[0], newInterval[0]), max(prev[1], newInterval[1])])
            else:
                ans.append(newInterval)
        return ans