def is_palindrome_permutation(s: str) -> bool:
  n = len(s)
  if n == 1:
    return True
  freq_map = dict()
  for c in s:
    if c.isalnum():
      freq_map[c] = freq_map.get(c, 0) + 1
  odd_flag = False
  for c, f in freq_map.items():
    if f & 1:
      if odd_flag or (n & 1):
        return False
      odd_flag = True
  return True


tc1 = 'abbab'
tc2 = 'race car'
tc3 = 'abab'
tc4 = 'aabbba'
print(is_palindrome_permutation(tc1) == False)
print(is_palindrome_permutation(tc2) == True)
print(is_palindrome_permutation(tc3) == True)
print(is_palindrome_permutation(tc4) == False)