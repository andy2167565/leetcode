class Trie:

    def __init__(self):
        self.children = {}

    def insert(self, word: str) -> None:
        # Reference: https://leetcode.com/problems/implement-trie-prefix-tree/discuss/362916/Simple-Python-solution-(beats-99-runtime-95-memory)/1486632
        cur = self.children  # Let cur point to children
        for c in word:
            if c not in cur:
                cur[c] = {}  # cur = {c: {}}
            cur = cur[c]  # cur is redirected to the value of key c
        cur['isWord'] = True  # Add to the most inner layer of children e.g. {'a': {'p': {'p': {'l': {'e': {'isWord': True}}}}}}

    def search(self, word: str) -> bool:
        cur = self.children
        for c in word:
            if c not in cur:
                return False
            cur = cur[c]
        return cur.get('isWord', False)

    def startsWith(self, prefix: str) -> bool:
        cur = self.children
        for c in prefix:
            if c not in cur:
                return False
            cur = cur[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
