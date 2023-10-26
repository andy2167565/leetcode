class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        import collections
        m, n = len(isWater), len(isWater[0])
        height = [[-1] * n for _ in range(m)]
        bfs = collections.deque([])
        for r in range(m):
            for c in range(n):
                if isWater[r][c]:
                    bfs.append((r, c))
                    height[r][c] = 0
        DIR = [0, 1, 0, -1, 0]
        while bfs:
            r, c = bfs.popleft()
            for i in range(4):
                nr, nc = r + DIR[i], c + DIR[i + 1]
                if 0 <= nr < m and 0 <= nc < n and height[nr][nc] == -1:
                    height[nr][nc] = height[r][c] + 1
                    bfs.append((nr, nc))
        return height
