class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        import collections
        m, n = len(grid), len(grid[0])
        if k >= m + n - 2:  # Manhattan Distance
            return m + n - 2
        step, seen, q = 0, set(), collections.deque([(0, 0, k)])  # Pair of (r, c)
        seen.add((0, 0, k))
        while q:
            for _ in range(len(q)):
                r, c, k = q.popleft()
                if r == m - 1 and c == n - 1:  # Reach to the bottom right cell
                    return step
                for dr, dc in (1, 0), (-1, 0), (0, 1), (0, -1):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n:
                        nk = k - grid[nr][nc]
                        new_state = (nr, nc, nk)
                        if nk >= 0 and new_state not in seen:
                            seen.add(new_state)
                            q.append(new_state)
            step += 1
        return -1
