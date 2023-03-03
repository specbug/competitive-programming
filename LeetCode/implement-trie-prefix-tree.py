class Trie:
    def __init__(self):
        self.is_word = False
        self.children = [None]*26

    def insert(self, word: str) -> None:
        node = self
        for c in word:
            x = ord(c)-ord('a')
            if node.children[x] is None:
                node.children[x] = Trie()
            node = node.children[x]
        node.is_word = True

    def search(self, word: str) -> bool:
        node = self
        for c in word:
            x = ord(c)-ord('a')
            if node.children[x] is None:
                return False
            node = node.children[x]
        return node.is_word

    def startsWith(self, prefix: str) -> bool:
        node = self
        for c in prefix:
            x = ord(c)-ord('a')
            if node.children[x] is None:
                return False
            node = node.children[x]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)