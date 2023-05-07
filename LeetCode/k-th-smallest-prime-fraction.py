import heapq

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        heap = []
        heapq.heapify(heap)
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                if len(heap) < k:
                    heapq.heappush(heap, (-arr[i]/arr[j], arr[i], arr[j]))
                else:
                    heapq.heappushpop(heap, (-arr[i]/arr[j], arr[i], arr[j]))
        ans = heapq.heappop(heap)
        return ans[1], ans[2]