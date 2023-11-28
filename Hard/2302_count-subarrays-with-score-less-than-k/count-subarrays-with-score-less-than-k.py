class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        ans = curr = start = 0
        for end, num in enumerate(nums):
            curr += num
            while curr * (end - start + 1) >= k:
                curr -= nums[start]
                start += 1
            ans += end - start + 1
        return ans
