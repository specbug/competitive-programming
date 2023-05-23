import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for _ in range(len(nums)+1)]
        freq_map = dict()
        for n in nums:
            freq_map[n] = freq_map.get(n, 0) + 1
        for i, v in freq_map.items():
            bucket[v].append(i)
        ans = []
        for i in range(len(bucket)-1, -1, -1):
            if bucket[i] is None:
                continue
            for b in bucket[i]:
                ans.append(b)
                k -= 1
                if k == 0:
                    break
            if k == 0:
                break
        return ans