class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        def dfs(path, t):
            if path:
                ans.add(path)
            for i in range(len(t)):
                dfs(path + t[i], t[:i] + t[i + 1:])
        ans = set()
        dfs('', tiles)
        return len(ans)
