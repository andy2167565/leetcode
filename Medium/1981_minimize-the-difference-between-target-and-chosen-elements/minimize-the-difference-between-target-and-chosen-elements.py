class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
# Reference: https://leetcode.com/problems/minimize-the-difference-between-target-and-chosen-elements/solutions/1418602/python-4-lines-solution-explained/
#======== <Solution 1> ========#
        sums = {0}
        for row in mat:
            sums = {x + s for x in row for s in sums}
        return min(abs(target - s) for s in sums)

#======== <Solution 2> ========#
        min_sum = sum(min(row) for row in mat)
        if min_sum > target:
            return min_sum - target
        sums = {0}
        for row in mat:
            sums = {x + s for x in row for s in sums if x + s <= 2 * target - min_sum}
        return min(abs(target - s) for s in sums)
