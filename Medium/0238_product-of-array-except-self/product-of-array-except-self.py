class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
# Reference: https://leetcode.com/problems/product-of-array-except-self/discuss/1597994/C%2B%2BPython-4-Simple-Solutions-w-Explanation-or-Prefix-and-Suffix-product-O(1)-space-approach
#======== <Solution 1> ========#
        import functools
        zero_count = nums.count(0)
        if zero_count > 1: return [0] * len(nums)
        product = functools.reduce(lambda a, b: a * (b if b else 1), nums, 1)
        for i, num in enumerate(nums):
            if zero_count:
                nums[i] = 0 if num else product
            else:
                nums[i] = product // num
        return nums

#======== <Solution 2> ========#
        import itertools, operator
        prefix = list(itertools.accumulate(nums, operator.mul))
        suffix = list(itertools.accumulate(nums[::-1], operator.mul))[::-1]
        for i in range(len(nums)):
            nums[i] = (prefix[i - 1] if i else 1) * (suffix[i + 1] if i < len(nums) - 1 else 1)
        return nums

#======== <Solution 3> ========#
        ans, suffix = [1] * len(nums), 1
        for i in range(1, len(nums)):
            ans[i] = ans[i - 1] * nums[i - 1]
        for i in range(len(nums) - 2, -1, -1):
            suffix *= nums[i + 1]
            ans[i] *= suffix
        return ans

#======== <Solution 4> ========#
        ans, suffix, prefix = [1] * len(nums), 1, 1
        for i in range(1, len(nums)):
            prefix *= nums[i - 1]
            ans[i] *= prefix
            suffix *= nums[~i + 1]
            ans[~i] *= suffix
        return ans
