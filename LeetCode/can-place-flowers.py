class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        l = len(flowerbed)
        z = 0
        s = 0
        f = (flowerbed[0] == 0)
        if l == 1:
            return int(not flowerbed[0]) >= n
        for i in flowerbed:
            if i == 1:
                s += max(((z+1)//2)-1, 0)
                s += int(f and z > 1)
                f = False
                z = 0
            else:
                z += 1
            if s >= n:
                return True
        s += max(((z+1)//2)-1, 0)
        s += int(flowerbed[-1] == 0 and z > 1)
        return s >= n
