class Trie:
    def __init__(self):
        self.recommendations = []
        self.children = [None]*26
        self.MAX_RECS = 3

    @classmethod
    def insert(cls, root, word):
        for c in word:
            x = ord(c)-ord('a')
            if root.children[x] is None:
                root.children[x] = Trie()
            root = root.children[x]
            if len(root.recommendations) < root.MAX_RECS:
                root.recommendations.append(word)
        root.is_word = True

    @classmethod
    def recommend(cls, root, query):
        recs = []
        for e, c in enumerate(query):
            x = ord(c)-ord('a')
            if root.children[x] is None:
                recs.extend([[] for _ in range(len(query)-e)])
                break
            root = root.children[x]
            recs.append(root.recommendations)
        return recs

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        root = Trie()
        for w in sorted(products):
            Trie.insert(root, w)
        return Trie.recommend(root, searchWord)
        