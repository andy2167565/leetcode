class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        # Reference: https://leetcode.com/problems/count-the-number-of-good-subarrays/solutions/3052559/java-c-python-sliding-window/
        import collections
        counter = collections.Counter()
        ans = pairs = i = 0
        for num in nums:
            pairs += counter[num]
            counter[num] += 1
            while pairs >= k:  # Current sliding window is a good subarray
                counter[nums[i]] -= 1
                pairs -= counter[nums[i]]
                i += 1
            ans += i
        return ans
