class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        mat = [[0]*n for _ in range(n)]
        for r1, c1, r2, c2 in queries:
            mat[r1][c1] += 1
            if r2 < n-1:
                mat[r2+1][c1] -= 1
            if c2 < n-1:
                mat[r1][c2+1] -= 1
            if r2 < n-1 and c2 < n-1:
                mat[r2+1][c2+1] += 1
        for i in range(1, n):
            mat[0][i] += mat[0][i-1]
            mat[i][0] += mat[i-1][0]
        for i in range(1, n):
            for j in range(1, n):
                mat[i][j] = mat[i][j] + mat[i-1][j] + mat[i][j-1] - mat[i-1][j-1]
        return mat