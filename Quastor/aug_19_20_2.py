"""
https://quastor.substack.com/p/coding-problem-facebook-exerts-influence
"""

def is_rotated(s, f):
  if len(s) != len(f):
    return False
  n = len(s)
  k = -1
  i = 0
  j = 0
  if f == s:
    return True
  while j < n:
    if f[j] == s[i]:
      if k == -1:
        k = j
      i += 1
      j += 1
    else:
      if k == -1:
        j += 1
      k = -1
      i = 0
  f = f[k:] + f[:k]
  return s == f

tc1 = ("CodingInterview", "erviewCodingInt")
tc2 = ("Test", "est")
tc3 = ("abcdabc", "abcabcd")
tc4 = ("abcd", "dcad")
tc5 = ("abcd", "cdaa")
tc6 = ("replit", "replit")

print(is_rotated(*tc1) == True)
print(is_rotated(*tc2) == False)
print(is_rotated(*tc3) == True)
print(is_rotated(*tc4) == False)
print(is_rotated(*tc5) == False)
print(is_rotated(*tc6) == True)