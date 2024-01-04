class Solution:
    def highestRankedKItems(self, grid: List[List[int]], pricing: List[int], start: List[int], k: int) -> List[List[int]]:
        import collections
        rank, dq = [], collections.deque([(0, start[0], start[1])])
        grid[start[0]][start[1]] *= -1  # Marked as visited
        while dq:
            step, r, c = dq.popleft()
            if pricing[0] <= -grid[r][c] <= pricing[1]:
                rank.append((step, -grid[r][c], r, c))
            for dr, dc in (1, 0), (-1, 0), (0, 1), (0, -1):
                nr, nc = r + dr, c + dc
                if len(grid) > nr >= 0 <= nc < len(grid[0]) and grid[nr][nc] > 0:
                    dq.append((step + 1, nr, nc))
                    grid[nr][nc] *= -1
        return [(r, c) for _, _, r, c in sorted(rank)[:k]]
