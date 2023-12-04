class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
# Reference: https://leetcode.com/problems/minimum-number-of-flips-to-convert-binary-matrix-to-zero-matrix/solutions/446342/java-python-3-convert-matrix-to-int-bfs-and-dfs-codes-w-explanation-comments-and-analysis/
#======== <Solution 1> ========#
        import collections
        m, n = len(mat), len(mat[0])
        start = sum(cell << (i * n + j) for i, row in enumerate(mat) for j, cell in enumerate(row))  # Map mat[i][j] to the (i * n + j)th bit of an binary int
        seen, dq = {start}, collections.deque([(start, 0)])
        while dq:
            curr, step = dq.popleft()
            if not curr:
                return step
            for i in range(m):
                for j in range(n):
                    nxt = curr
                    for r, c in (i, j), (i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j):  # Flip the cell and its four neighbors
                        if m > r >= 0 <= c < n:
                            nxt ^= 1 << (r * n + c)
                    if nxt not in seen:
                        seen.add(nxt)
                        dq.append((nxt, step + 1))
        return -1

#======== <Solution 2> ========#
        m, n = len(mat), len(mat[0])
        start = sum(cell << i * n + j for i, row in enumerate(mat) for j, cell in enumerate(row))
        seenSteps, stack = {start: 0}, [(start, 0)]
        while stack:
            curr, step = stack.pop()
            for i in range(m):
                for j in range(n):
                    nxt = curr
                    for r, c in (i, j), (i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j):
                        if m > r >= 0 <= c < n:
                            nxt ^= 1 << (r * n + c)
                    if seenSteps.get(nxt, float('inf')) > step + 1:
                        seenSteps[nxt] = step + 1
                        stack.append((nxt, step + 1))
        return seenSteps.get(0, -1)
