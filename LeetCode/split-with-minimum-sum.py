class Solution:
    def splitNum(self, num: int) -> int:
        nums = sorted(str(num))
        n1 = ''
        n2 = ''
        for e, i in enumerate(nums):
            if e&1:
                n2 += i
            else:
                n1 += i
        return int(n1)+int(n2)