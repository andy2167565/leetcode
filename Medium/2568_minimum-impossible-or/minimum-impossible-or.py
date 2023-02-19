class Solution:
    def minImpossibleOR(self, nums: List[int]) -> int:
# Reference: https://leetcode.com/problems/minimum-impossible-or/solutions/3201897/java-c-python-pow-of-2/
#======== <Solution 1> ========#
        nums.sort()
        x = 1
        for i in nums:
            if x == i:
                x *= 2
        return x

#======== <Solution 2> ========#
        nums = set(nums)
        return next(1 << i for i in range(31) if (1 << i) not in nums)
