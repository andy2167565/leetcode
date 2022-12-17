class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
#======== <Solution 1> ========#
        # Reference: https://leetcode.com/problems/pacific-atlantic-water-flow/solutions/90739/python-dfs-bests-85-tips-for-all-dfs-in-matrix-question/
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        m, n = len(heights), len(heights[0])
        pacific, atlantic = set(), set()
        def dfs(i, j, visited):
            visited.add((i, j))
            for dx, dy in directions:
                x, y = i + dx, j + dy
                if 0 <= x < m and 0 <= y < n and (x, y) not in visited and heights[i][j] <= heights[x][y]:
                    dfs(x, y, visited)
        for i in range(m):
            dfs(i, 0, pacific)  # (i, 0) must in pacific
            dfs(i, n - 1, atlantic)  # (i, n - 1) must in atlantic
        for j in range(n):
            dfs(0, j, pacific)  # (0, j) must in pacific
            dfs(m - 1, j, atlantic)  # (m - 1, j) must in atlantic
        return list(pacific & atlantic)

#======== <Solution 2> ========#
        # Reference: https://leetcode.com/problems/pacific-atlantic-water-flow/solutions/1126782/python-simple-bfs-explained/
        import collections
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        m, n = len(heights), len(heights[0])
        pacific, atlantic = set(), set()
        def bfs(visited):
            dq = collections.deque(visited)
            while dq:
                i, j = dq.popleft()
                for dx, dy in directions:
                    x, y = i + dx, j + dy
                    if 0 <= x < m and 0 <= y < n and (x, y) not in visited and heights[i][j] <= heights[x][y]:
                        dq.append((x, y))
                        visited.add((x, y))
            return visited
        for i in range(m):
            pacific.add((i, 0))
            atlantic.add((i, n - 1))
        for j in range(n):
            pacific.add((0, j))
            atlantic.add((m - 1, j))
        return list(bfs(pacific) & bfs(atlantic))
