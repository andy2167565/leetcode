class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
#======== <Solution 1> ========#
        vals = []
        for row in grid:
            vals += row
        vals.sort(reverse=True)
        median, ans = vals[len(vals) // 2], 0
        for val in vals:
            ops, r = divmod(abs(val - median), x)
            if r:
                return -1
            ans += ops
        return ans

#======== <Solution 2> ========#
        vals = [val for row in grid for val in row]
        if len(set(val % x for val in vals)) > 1:  # More than one kind of remainder
            return -1
        median = sorted(vals)[len(vals) // 2]
        return sum(abs(val - median) // x for val in vals)
