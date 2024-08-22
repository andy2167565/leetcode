class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        # Reference: https://leetcode.com/problems/stone-game-ii/solutions/345230/java-python-dp-solution/
        import functools
        n = len(piles)
        for i in range(n - 2, -1, -1):
            piles[i] += piles[i + 1]  # piles[i]: Total stones of piles[i:]

        @functools.cache
        def dfs(i, m):  # dfs(i, m): The maximum stones the current player can get from piles[i:] with M = m
            return piles[i] - (min(dfs(i + x, max(m, x)) for x in range(1, 2 * m + 1)) if i + 2 * m < n else 0)

        return dfs(0, 1)
