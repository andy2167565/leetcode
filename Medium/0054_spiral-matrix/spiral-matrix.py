class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
#======== <Solution 1> ========#
        # Reference: https://leetcode.com/problems/spiral-matrix/discuss/394774/python-3-solution-for-spiral-matrix-one-of-the-most-easiest-you-will-never-forget/1026252
        m, n, ans = len(matrix), len(matrix[0]), []
        top, left, bottom, right = 0, 0, m - 1, n - 1
        while top < bottom and left < right:
            for j in range(left, right):
                ans.append(matrix[top][j])
            for i in range(top, bottom):
                ans.append(matrix[i][right])
            for j in range(right, left, -1):
                ans.append(matrix[bottom][j])
            for i in range(bottom, top, -1):
                ans.append(matrix[i][left])
            top, left, bottom, right = top + 1, left + 1, bottom - 1, right - 1
        if len(ans) < m * n:  # Append the inner remaining matrix, which is either 1 x n or m x 1
            for i in range(top, bottom + 1):
                for j in range(left, right + 1):
                    ans.append(matrix[i][j])
        return ans

#======== <Solution 2> ========#
        ans = []
        while matrix:
            ans += matrix.pop(0)
            if matrix and matrix[0]:  # For m x 1 matrix, each matrix[i] is empty after the first round of row.pop()
                for row in matrix:
                    ans.append(row.pop())
            if matrix:
                ans += matrix.pop()[::-1]
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    ans.append(row.pop(0))
        return ans

#======== <Solution 3> ========#
        # Reference: https://leetcode.com/problems/spiral-matrix/discuss/999388/95.41-faster-solution
        ans = []
        while matrix:
            ans += matrix.pop(0)
            matrix = list(zip(*matrix))[::-1]  # Transpose
        return ans

#======== <Solution 4> ========#
        # Reference: https://leetcode.com/problems/spiral-matrix/discuss/20571/1-liner-in-Python-%2B-Ruby
        return matrix and [*matrix.pop(0)] + self.spiralOrder([*zip(*matrix)][::-1])

#======== <Solution 5> ========#
        # Reference: https://leetcode.com/problems/spiral-matrix/discuss/1466413/Python-simulate-process-explained
        m, n, ans = len(matrix), len(matrix[0]), []
        x, y, dx, dy = 0, 0, 1, 0  # (x, y): Coordinate; (dx, dy): Direction of movement
        for _ in range(m * n):
            if not 0 <= x + dx < n or not 0 <= y + dy < m or matrix[y + dy][x + dx] == '*':  # Rotate if next (x, y) is out of boundary or next element has already been visited
                dx, dy = -dy, dx
            ans.append(matrix[y][x])
            matrix[y][x] = '*'  # Marked as visited
            x, y = x + dx, y + dy
        return ans
