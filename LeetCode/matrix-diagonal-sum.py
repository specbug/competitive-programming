class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        i = 0
        j = len(mat[0])-1
        s = 0
        for r in range(len(mat)):
            s += mat[r][i] + mat[r][j]
            if i == j:
                s -= mat[r][i]
            i += 1
            j -= 1
        return s
