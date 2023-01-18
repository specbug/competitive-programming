class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ans = []
        c = 1
        for i in range(len(digits)-1, -1, -1):
            x = digits[i] + c
            ans.append(x%10)
            c = 0
            if x >= 10:
                c += 1
            else:
                ans += digits[:i][::-1]
                break
        if c:
            ans.append(c)
        return ans[::-1]