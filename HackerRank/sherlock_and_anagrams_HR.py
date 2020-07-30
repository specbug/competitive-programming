import itertools

def sherlockAndAnagrams(s):
	ss = ''.join([str(i) for i in range(len(s))])
	all_comb = [[''.join(list(p)) for p in itertools.combinations(ss, i)] for i in range(2, len(ss)+1)]
	n_anagrams = 0
	for c in all_comb:
		print(c)
		# for k in c:
		# 	print(list(itertools.permutations(k, 2)))
		# 	print()
		# print()

	return n_anagrams

t = int(input())

for _ in range(t):
	s = input().rstrip()
	print(sherlockAndAnagrams(s))