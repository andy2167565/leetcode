class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
# Reference: https://leetcode.com/problems/count-number-of-nice-subarrays/solutions/419378/java-c-python-sliding-window-o-1-space/
#======== <Solution 1> ========#
        def atMost(k):
            ans = l = 0
            for r, num in enumerate(nums):
                k -= num % 2
                while k < 0:
                    k += nums[l] % 2
                    l += 1
                ans += r - l + 1
            return ans
        return atMost(k) - atMost(k - 1)

#======== <Solution 2> ========#
        ans = l = count = 0
        for num in nums:
            if num & 1:
                k -= 1
                count = 0
            while not k:
                k += nums[l] & 1
                l += 1
                count += 1
            ans += count
        return ans
