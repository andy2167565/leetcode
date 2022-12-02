class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Reference: https://leetcode.com/problems/word-search/discuss/27660/Python-dfs-solution-with-comments.
        def dfs(r, c, i):  # Check if word[i:] exists starting at (r, c)
            if i == word_len:  # All the characters of word are found
                return True
            if 0 <= r < m and 0 <= c < n and word[i] == board[r][c]:  # Character i is found, check the remaining part
                board[r][c] = '#'  # Marked as visited
                for dr, dc in directions:
                    if dfs(r + dr, c + dc, i + 1):
                        return True
                board[r][c] = word[i]  # Resume for later search
            return False
        m, n, word_len, directions = len(board), len(board[0]), len(word), [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for r in range(m):
            for c in range(n):
                if dfs(r, c, 0):
                    return True
        return False
