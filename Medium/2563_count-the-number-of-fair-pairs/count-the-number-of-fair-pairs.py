class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
#======== <Solution 1> ========#
        nums.sort()
        ans = 0
        lo = hi = len(nums) - 1
        for i, num in enumerate(nums):
            while lo >= 0 and num + nums[lo] >= lower:  # Find lower bound (not included)
                lo -= 1
            while hi >= 0 and num + nums[hi] > upper:  # Find upper bound (included)
                hi -= 1
            ans += hi - lo
            if lo < i <= hi:  # Remove the pair (i, i)
                ans -= 1
        return ans // 2  # Each pair has been counted twice

#======== <Solution 2> ========#
        import bisect
        nums.sort()
        ans = 0
        for i in range(len(nums) - 1, -1, -1):
            l = bisect.bisect_left(nums, lower - nums[i], lo=0, hi=i)
            u = bisect.bisect_right(nums, upper - nums[i], lo=0, hi=i)
            ans += u - l
        return ans
