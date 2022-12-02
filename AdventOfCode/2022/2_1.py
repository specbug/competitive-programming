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
    rule_map = {
        "A": "rock",
        "B": "paper",
        "C": "scissor",
        "X": "rock",
        "Y": "paper",
        "Z": "scissor",
    }
    score_map = {"X": 1, "Y": 2, "Z": 3}
    res_map = {-1: 3, 0: 0, 1: 6}
    ans = 0
    with open(file) as f:
        for l in f.readlines():
            a, b = l.split()
            win = cmp(rule_map[a], rule_map[b])
            ans += score_map[b] + res_map[win]
    return ans


file = sys.argv[1]
print(main(file))
