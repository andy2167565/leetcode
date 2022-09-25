class Solution:
    def maxProduct(self, nums: List[int]) -> int:
#======== <Solution 1> ========#
        # Reference: https://leetcode.com/problems/maximum-product-subarray/discuss/48276/Python-solution-with-detailed-explanation
        max_prod = min_prod = ans = nums[0]
        for num in nums[1:]:
            min_prod, _, max_prod = sorted([num, max_prod * num, min_prod * num])
            ans = max(ans, max_prod)
        return ans

# Reference: https://leetcode.com/problems/maximum-product-subarray/discuss/183483/JavaC%2B%2BPython-it-can-be-more-simple
#======== <Solution 2> ========#
        suffix = nums[::-1]
        for i in range(1, len(nums)):
            nums[i] *= nums[i - 1] or 1
            suffix[i] *= suffix[i - 1] or 1
        return max(nums + suffix)

#======== <Solution 3> ========#
        prefix, suffix, ans = 0, 0, float('-inf')
        for i in range(len(nums)):
            prefix = (prefix or 1) * nums[i]
            suffix = (suffix or 1) * nums[~i]
            ans = max(ans, prefix, suffix)
        return ans
