from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        tracker = set()
        for n in nums:
            l_tracker = len(tracker)
            tracker.add(n)
            if len(tracker) == l_tracker:
                return True
        return False