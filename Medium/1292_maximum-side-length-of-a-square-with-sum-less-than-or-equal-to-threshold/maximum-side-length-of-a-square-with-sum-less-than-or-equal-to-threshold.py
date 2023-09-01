class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        # Reference: https://leetcode.com/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/solutions/698422/python-prefix-sum-explanation-with-diagram/
        m, n = len(mat), len(mat[0])
        prefix = [[0 for _ in range(n + 1)] for _ in range(m + 1)]  # Zero-padding on the topmost row and leftmost column
        for i in range(m):  # Calculate the prefix sum for each cell
            for j in range(n):
                prefix[i + 1][j + 1] = prefix[i][j + 1] + prefix[i + 1][j] - prefix[i][j] + mat[i][j]
        max_side = 0
        for i in range(m):
            for j in range(n):
                if min(i, j) >= max_side:  # Check if rectangle or square from [i - max_side, j - max_side] to [i, j] <= threshold
                    curr = prefix[i + 1][j + 1]
                    top = prefix[i - max_side][j + 1]
                    left = prefix[i + 1][j - max_side]
                    topLeft = prefix[i - max_side][j - max_side]
                    total = curr - top - left + topLeft
                    if total <= threshold:
                        max_side += 1
        return max_side
