class Solution:
    def xorBeauty(self, nums: List[int]) -> int:
# Reference (Explanation): https://leetcode.com/problems/find-xor-beauty-of-array/solutions/3015014/why-just-xor-of-all-numbers-works/
#======== <Solution 1> ========#
        ans = nums[0]
        for num in nums[1:]:
            ans ^= num
        return ans

#======== <Solution 2> ========#
        import functools, operator
        return functools.reduce(operator.xor, nums)
