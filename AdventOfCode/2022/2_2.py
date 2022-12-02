import sys


def cmp(a, b):
	rules = {"rock": "scissor", "paper": "rock", "scissor": "paper"}
	if a == b:
		return -1
	if rules[a] == b:
		return 0
	else:
		return 1


def main(file):
	rules = {"rock": "scissor", "paper": "rock", "scissor": "paper"}
	rule_map = {"A": "rock", "B": "paper", "C": "scissor"}
	score_map = {"rock": 1, "paper": 2, "scissor": 3}
	action_map = {"X": 0, "Y": -1, "Z": 1}
	res_map = {-1: 3, 0: 0, 1: 6}
	ans = 0
	with open(file) as f:
		for l in f.readlines():
			a, b = l.split()
			if action_map[b] == -1:
				_score = score_map[rule_map[a]]
			elif action_map[b] == 0:
				_score = score_map[rules[rule_map[a]]]
			else:
				_score = score_map[
					next(iter(k for k, v in rules.items() if v == rule_map[a]))
				]
			ans += res_map[action_map[b]] + _score
	return ans


file = sys.argv[1]
print(main(file))
