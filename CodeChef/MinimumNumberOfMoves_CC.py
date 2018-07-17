w = []
c = 0
t = int(input())
for i in range(t):
  n = int(input())
  w = list(map(int, input().split()))
  c = sum(w)-n*min(w)
  print(c)
 
