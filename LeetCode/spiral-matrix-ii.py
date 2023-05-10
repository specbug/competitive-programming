class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        i, j = 0, 0
        di, dj = 0, 1
        A = [[0]*n for _ in range(n)]
        for k in range(n*n):
            A[i][j] = k+1
            if A[(i+di)%n][(j+dj)%n]:
                di, dj = dj, -di
            i += di
            j += dj
        return A