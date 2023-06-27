class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        # Reference: https://leetcode.com/problems/spiral-matrix-iii/solutions/158970/c-java-python-1-1-2-2-3-3-steps/
        ans, dr, dc, n = [], 0, 1, 0
        while len(ans) < rows * cols:
            for _ in range(n // 2 + 1):  # Number of steps for current side
                if 0 <= rStart < rows and 0 <= cStart < cols:
                    ans.append([rStart, cStart])
                rStart, cStart = rStart + dr, cStart + dc
            dr, dc, n = dc, -dr, n + 1  # Turn right
        return ans
