class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        ord_map = dict()
        l = len(words)
        for i, c in enumerate(order):
            ord_map[c] = i
        for w in range(l-1):
            for i in range(len(words[w])):
                if i >= len(words[w+1]):
                    return False
                if ord_map[words[w][i]] != ord_map[words[w+1][i]]:
                    if ord_map[words[w][i]] > ord_map[words[w+1][i]]:
                        return False
                    break
        return True

