class Solution:
    def missingNumber(self, nums: List[int]) -> int:
#======== <Solution 1> ========#
        return list(set(range(len(nums)+1)) - set(nums))[0]

#======== <Solution 2> ========#
        return sum(range(len(nums)+1)) - sum(nums)

#======== <Solution 3> ========#
        return len(nums) * (len(nums)+1) // 2 - sum(nums)

#======== <Solution 4> ========#
        return reduce(lambda x, y: x ^ y, list(range(len(nums)+1)) + nums)
