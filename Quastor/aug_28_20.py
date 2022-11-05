import random

def get_sqrt_recursive(x, l, r):
      if x < 2:
          return x
      mid = l + (r - l) // 2
      if mid*mid <= x:
          if (mid+1)*(mid+1) > x:
              return mid
          else:
              return get_sqrt_recursive(x, mid+1, r)
      else:
          return get_sqrt_recursive(x, l, mid-1)
      
  
def my_sqrt(x: int) -> int:
    if x < 2:
        return x
    return get_sqrt_recursive(x, 1, x)

for _ in range(10):
  x = random.choice(range(int(1e8)))
  if my_sqrt(x) != int(x**(1/2)):
    print(f'TC failed for x = {x}')
  else:
    print(f'TC passed for x = {x}')
        