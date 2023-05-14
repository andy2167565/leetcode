class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
#======== <Solution 1> ========#
        return sum(max(col) for col in zip(*[sorted(row) for row in nums]))

#======== <Solution 2> ========#
        return sum(map(max, zip(*map(sorted, nums))))
