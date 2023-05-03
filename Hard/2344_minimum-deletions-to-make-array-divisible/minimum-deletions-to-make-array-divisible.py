class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
# Reference: https://leetcode.com/problems/minimum-deletions-to-make-array-divisible/solutions/2292651/java-c-python-gcd-o-n-m-log/
#======== <Solution 1> ========#
        import math
        g = math.gcd(*numsDivide)
        for i, num in enumerate(sorted(nums)):
            if not g % num:
                return i
        return -1

#======== <Solution 2> ========#
        import math
        g = math.gcd(*numsDivide)
        return next((i for i, num in enumerate(sorted(nums)) if not g % num), -1)

#======== <Solution 3> ========#
        import math
        g = math.gcd(*numsDivide)
        m = min((num for num in nums if not g % num), default=0)
        return sum(num < m for num in nums) if m else -1
