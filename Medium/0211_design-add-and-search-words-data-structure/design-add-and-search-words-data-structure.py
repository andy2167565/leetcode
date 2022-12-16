class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        node = self.trie
        for c in word:
            node = node.setdefault(c, {})  # Create a nested dict for each word e.g. trie = {'b': {'a': {'d': {'$': True}}}}
        node['$'] = True

    def search(self, word: str) -> bool:
        return self.searchNode(self.trie, word)

    def searchNode(self, node, word: str) -> bool:
        for i, c in enumerate(word):
            if c == '.':
                return any(self.searchNode(node[ch], word[i + 1:]) for ch in node if ch != '$')  # Search every branch of current level
            if c not in node: return False  # Check c at current level
            node = node[c]  # Move to next level
        return '$' in node


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
