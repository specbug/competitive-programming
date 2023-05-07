class Solution:
    def average(self, salary: List[int]) -> float:
        mx = salary[0]
        mn = salary[0]
        t = 0
        n = len(salary)
        for s in salary:
            mx = max(mx, s)
            mn = min(mn, s)
            t += s
        return (t-mx-mn)/(n-2)