class Solution:
    def coloredCells(self, n: int) -> int:
# Reference: https://leetcode.com/problems/count-total-number-of-colored-cells/solutions/3256196/java-c-python-cut-and-combine-o-1/
#======== <Solution 1> ========#
        return n * n + (n - 1) * (n - 1)

#======== <Solution 2> ========#
        return n * (n - 1) * 2 + 1
