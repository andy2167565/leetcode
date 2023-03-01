class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def search(node, r, c):
            if 'word' in node:  # A complete word has been found
                word = node.pop('word')
                found.append(word)
                remove(word)  # Remove word from trie
            if 0 <= r < m and 0 <= c < n and board[r][c]:
                char = board[r][c]
                board[r][c] = None  # Marked as visited
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if char in node:
                        search(node[char], row, col)
                board[r][c] = char  # Restore to original state

        def remove(word):
            node, parents = trie, []
            for char in word:
                parents.append(node)
                node = node[char]
            for i in range(len(parents) - 1, -1, -1):
                if node == {}:
                    parents[i].pop(word[i])
                    node = parents[i]
                else:  # Parents are shared by other words
                    break

        m, n = len(board), len(board[0])
        trie, found, directions = {}, [], [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for word in words:  # Store all words in trie format
            node = trie
            for char in word:
                node = node.setdefault(char, {})
            node['word'] = word  # e.g. word = 'oath', trie = {'o': {'a': {'t': {'h': {'word': 'oath'}}}}}
        for r in range(m):
            for c in range(n):
                if len(found) < len(words):
                    search(trie, r, c)
        return found
