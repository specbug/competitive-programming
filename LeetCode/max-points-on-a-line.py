class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        l = len(points)
        ans = 0
        if l == 1:
            return 1
        for i in range(l):
            slopes = dict()
            x1, y1 = points[i]
            offset = 0
            for j in range(i, l):
                x2, y2 = points[j]
                if x1 == x2 and y1 == y2:
                    offset += 1
                    continue
                if x1 == x2:
                    slope = 'i'
                else:
                    slope = (y2-y1)/(x2-x1) # (y2-y1)/(x2-x1)
                slopes[slope] = slopes.get(slope, 0) + 1
            if len(slopes) > 0:
                ans = max(ans, max(slopes.values())+offset)
        return ans