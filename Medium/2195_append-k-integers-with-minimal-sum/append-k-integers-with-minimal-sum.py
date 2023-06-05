class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        ans = k * (k + 1) // 2  # Start from the sum of 1 to k
        for num in sorted(set(nums)):
            if num <= k:  # num is in the range of 1 to k
                k += 1  # Need to add (k + 1) instead of num
                ans += k - num  # Add the difference between num and (k + 1)
        return ans
