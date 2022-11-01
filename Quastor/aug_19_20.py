"""
https://quastor.substack.com/p/microsoft-interview-question-oracle
"""

def zero_mat(A):
  n = len(A)
  if n <= 1:
    return A
  m = len(A[0])
  for i in range(1, n):
    for j in range(1, m):
      if A[i][j] == 0:
        A[0][j] = -abs(A[0][j])
        A[i][0] = -abs(A[i][0])
  row_flag = False
  col_flag = False
  for i in range(1, n):
    if A[i][0] > 0:
      continue
    if A[i][0] == 0:
      col_flag = True
    for j in range(m):
      A[i][j] = 0
  for j in range(1, m):
    if A[0][j] > 0:
      continue
    if A[0][j] == 0:
      row_flag = True
    for i in range(n):
      A[i][j] = 0
  if row_flag:
    for j in range(m):
      A[0][j] = 0
  if col_flag:
    for i in range(n):
      A[i][0] = 0
  return A


test1 = [[1,2,3,4],[5,0,7,8],[6,1,1,2],[2,3,4,0]]
ans1 = [[1,0,3,0],[0,0,0,0],[6,0,1,0],[0,0,0,0]]
test2 = []
ans2 = []
test3 = [1]
ans3 = [1]
test3 = [0]
ans3 = [0]

print(zero_mat(test1) == ans1)
print(zero_mat(test2) == ans2)
print(zero_mat(test3) == ans3)
print(zero_mat(test4) == ans4)