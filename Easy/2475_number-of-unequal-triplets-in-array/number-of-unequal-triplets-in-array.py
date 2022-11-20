class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
#======== <Solution 1> ========#
        ans = 0
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                for k in range(j + 1, len(nums)):
                    if nums[i] != nums[j] and nums[i] != nums[k] and nums[j] != nums[k]:
                        ans += 1
        return ans

#======== <Solution 2> ========#
        # Reference: https://leetcode.com/problems/number-of-unequal-triplets-in-array/discuss/2831702/O(n)
        import collections
        counter = collections.Counter(nums)
        ans, l, r = 0, 0, len(nums)
        for num, count in counter.items():
            r -= count
            ans += l * count * r
            l += count
        return ans
