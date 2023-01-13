from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        n = len(nums)
        if n == 1:
            return nums[0]
        k = min(n, k)
        queue = deque()
        ans = []
        for i in range(k):
            while queue and nums[i] > nums[queue[-1]]:
                queue.pop()
            queue.append(i)
        ans.append(nums[queue[0]])

        for i in range(n-k):
            if queue[0] == i:
                queue.popleft()
            while queue and nums[i+k] > nums[queue[-1]]:
                queue.pop()
            queue.append(i+k)
            ans.append(nums[queue[0]])
        return ans