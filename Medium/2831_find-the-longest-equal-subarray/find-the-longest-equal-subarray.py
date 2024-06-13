class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        # Reference: https://leetcode.com/problems/find-the-longest-equal-subarray/solutions/3934172/java-c-python-one-pass-sliding-window-o-n/
        import collections
        ans = i = 0
        counter = collections.Counter()
        for j in range(len(nums)):  # Sliding window
            counter[nums[j]] += 1
            ans = max(ans, counter[nums[j]])
            if j - i + 1 - ans > k:  # The number of deleted elements is more than k
                counter[nums[i]] -= 1
                i += 1
        return ans
