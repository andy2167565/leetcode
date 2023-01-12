class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
# Reference: https://leetcode.com/problems/minimum-knight-moves/solutions/947138/python-3-bfs-dfs-math-explanation/
#======== <Solution 1> ========#
        import collections
        x, y, visited, queue, directions = abs(x), abs(y), set((0, 0)), collections.deque([(0, 0, 0)]), [(1, 2), (2, 1), (1, -2), (2, -1), (-1, 2), (-2, 1)]  # No need to have (-1, -2) and (-2, -1) otherwise we will move backwards in the first quadrant
        while queue:
            a, b, step = queue.popleft()
            if (a, b) == (x, y): return step
            for dx, dy in directions:
                i, j = a + dx, b + dy
                if (i, j) not in visited and -1 <= i <= x + 2 and -1 <= j <= y + 2:
                    visited.add((i, j))
                    queue.append((i, j, step + 1))

#======== <Solution 2> ========#
        @cache
        def dfs(x, y):
            if not x + y: return 0  # Reach the origin
            if x + y == 2: return 2  # Reach (0, 2), (2, 0) or (1, 1)
            return min(dfs(abs(x - 1), abs(y - 2)), dfs(abs(x - 2), abs(y - 1))) + 1
        return dfs(abs(x), abs(y))  # Only check (x, y) in the first quadrant

#======== <Solution 3> ========#
        # Reference 1: https://leetcode.com/problems/minimum-knight-moves/solutions/392053/here-is-how-i-get-the-formula-with-graphs/
        # Reference 2: https://leetcode.com/problems/minimum-knight-moves/solutions/387036/o-1-formula/
        x, y = abs(x), abs(y)  # Symmetry for axes
        if x < y: x, y = y, x  # Symmetry for diagonal
        if x == 1 and y == 0: return 3
        if x == 2 and y == 2: return 4
        delta = x - y
        if y > delta: return delta - 2 * int((delta - y) // 3)
        return delta - 2 * int((delta - y) // 4)
