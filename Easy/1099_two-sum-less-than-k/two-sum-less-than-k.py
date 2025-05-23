class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans, lo, hi = -1, 0, len(nums) - 1
        while lo < hi:
            curr = nums[lo] + nums[hi]
            if curr < k:
                lo += 1
                ans = max(ans, curr)
            else:
                hi -= 1
        return ans
