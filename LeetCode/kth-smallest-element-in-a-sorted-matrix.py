import heapq

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        m = len(matrix)
        n = len(matrix[0])
        for r in range(min(m, k)):
            heapq.heappush(heap, (matrix[r][0], r, 0))
        for i in range(k):
            x, r, c = heapq.heappop(heap)
            if c < n-1:
                heapq.heappush(heap, (matrix[r][c+1], r, c+1))
        return x