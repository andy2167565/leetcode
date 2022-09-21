class Solution:
    def arraySign(self, nums: List[int]) -> int:
# My Post: https://leetcode.com/problems/sign-of-the-product-of-an-array/discuss/2604867/Python-One-liner-without-if-else-Statement
#======== <Solution 1> ========#
        return (sum(i < 0 for i in nums) % 2 * (-2) + 1) * (0 not in nums)

#======== <Solution 2> ========#
        sign = 1
        for i in nums:
            if not i:
                return 0
            if i < 0:
                sign = -sign
        return sign
