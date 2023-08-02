class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        import itertools
        dp = [[True] * n + [False] for _ in range(m)] + [[False] * n]  # Add an extra border so no need the coordinate validity checks
        for row, col in guards + walls:  # Occupied cells
            dp[row][col] = False
        for dr, dc in itertools.pairwise([0, 1, 0, -1, 0]):
            for row, col in guards:
                while dp[row := row + dr][col := col + dc] is not False:  # Unoccupied cell
                    dp[row][col] = 0  # The cell is guarded
        return sum(map(sum, dp))
