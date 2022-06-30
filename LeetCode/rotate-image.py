from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n // 2 + n % 2):
            rs = cs = i
            re = ce = n-1-i
            if rs >= re:
                break
            for k in range(n-1):
                if rs+k >= re:
                    continue
                matrix[rs][cs+k], matrix[re-k][cs] = matrix[re-k][cs], matrix[rs][cs+k]
                matrix[re-k][cs], matrix[re][ce-k] = matrix[re][ce-k], matrix[re-k][cs]
                matrix[re][ce-k], matrix[rs+k][ce] = matrix[rs+k][ce], matrix[re][ce-k]