class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        q, seen = [(0, 0, 0, 1, 0)], set()
        for r1, r2, c1, c2, move in q:
            if (r1, r2, c1, c2) == (m - 1, m - 1, n - 2, n - 1):  # Reach the target
                return move
            if (r1, r2, c1, c2) not in seen:
                seen.add((r1, r2, c1, c2))
                for x1, x2, y1, y2 in (r1, r2, c1 + 1, c2 + 1), (r1 + 1, r2 + 1, c1, c2):  # Move right or down
                    if x2 < m and y2 < n and not grid[x1][y1] + grid[x2][y2]:
                        q.append((x1, x2, y1, y2, move + 1))
                if r1 == r2 and r1 + 1 < m and not grid[r1 + 1][c1] + grid[r1 + 1][c2]:  # Rotate clockwise
                    q.append((r1, r1 + 1, c1, c1, move + 1))
                if c1 == c2 and c1 + 1 < n and not grid[r1][c1 + 1] + grid[r2][c1 + 1]:  # Rotate counterclockwise
                    q.append((r1, r1, c1, c1 + 1, move + 1))
        return -1
