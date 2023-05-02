class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        import collections
        m, n, directions = len(maze), len(maze[0]), [(0, 1), (0, -1), (1, 0), (-1, 0)]
        dq = collections.deque([(*entrance, 0)])
        maze[entrance[0]][entrance[1]] = '+'  # Marked as visited
        while dq:
            i, j, steps = dq.popleft()
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and maze[ni][nj] == '.':
                    if not ni * nj or ni == m - 1 or nj == n - 1:  # Reached the border
                        return steps + 1
                    maze[ni][nj] = '+'  # Need to mark the cell immediately when occurred or it may be visited twice or more
                    dq.append((ni, nj, steps + 1))
        return -1
