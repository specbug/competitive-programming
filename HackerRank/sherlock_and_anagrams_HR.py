import itertools

def sherlockAndAnagrams(s):
	fc = {}
	rev_fc = {}

	rev_s = s[::-1]
	for i in range(len(s)):
		for j in range(len(s[i:])):
			fc[s[i: i+j+1]] = fc.get(s[i: i+j+1], 0) + 1
			rev_fc[rev_s[i: i+j+1]] = rev_fc.get(rev_s[i: i+j+1], 0) + 1

	print(fc)
	print()
	print(rev_fc)
	return None

t = int(input())

for _ in range(t):
	s = input().rstrip()
	print(sherlockAndAnagrams(s))