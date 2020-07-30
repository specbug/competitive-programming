import numpy as np

n, m = map(int, input().split())
print(str(np.eye(n, m)).replace('1', ' 1').replace('0', ' 0'))