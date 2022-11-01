class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
# Reference: https://leetcode.com/problems/01-matrix/discuss/1369741/C%2B%2BJavaPython-BFS-DP-solutions-with-Picture-Clean-and-Concise-O(1)-Space
#======== <Solution 1> ========#
        import collections
        m, n = len(mat), len(mat[0])
        neighbors = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        q = collections.deque([])
        # Collect coordinate of cells with value 0
        for r in range(m):
            for c in range(n):
                if not mat[r][c]:
                    q.append((r, c))
                else:
                    mat[r][c] = -1  # Marked as not processed yet
        # Search for unprocessed neighbors of the current processing cell and push into the queue
        while q:
            r, c = q.popleft()
            for i, j in neighbors:
                nr, nc = r + i, c + j
                if 0 <= nr < m and 0 <= nc < n and mat[nr][nc] == -1:
                    mat[nr][nc] = mat[r][c] + 1
                    q.append((nr, nc))
        return mat

#======== <Solution 2> ========#
        m, n = len(mat), len(mat[0])
        # Compute distance based on top and left neighbors from top-left to bottom-right
        for r in range(m):
            for c in range(n):
                if mat[r][c]:
                    top = mat[r - 1][c] if r else float('inf')
                    left = mat[r][c - 1] if c else float('inf')
                    mat[r][c] = min(top, left) + 1
        # Compute distance based on bottom and right neighbors from bottom-right to top-left
        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                if mat[r][c]:
                    bottom = mat[r + 1][c] if r < m - 1 else float('inf')
                    right = mat[r][c + 1] if c < n - 1 else float('inf')
                    mat[r][c] = min(mat[r][c], bottom + 1, right + 1)
        return mat
