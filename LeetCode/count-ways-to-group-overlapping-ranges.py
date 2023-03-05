class Solution:
    def countWays(self, ranges: List[List[int]]) -> int:
        MOD = int(1e9)+7
        ranges = sorted(ranges, key=lambda x: x[0])
        for i in range(1, len(ranges)):
            if ranges[i][0] <= ranges[i-1][1]:
                ranges[i][0] = min(ranges[i-1][0], ranges[i][0])
                ranges[i][1] = max(ranges[i-1][1], ranges[i][1])
                ranges[i-1] = None
        ranges = [r for r in ranges if r is not None]
        return 2**len(ranges)%MOD