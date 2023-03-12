class Solution:
    def beautifulSubarrays(self, nums: List[int]) -> int:
        # Reference: https://leetcode.com/problems/count-the-number-of-beautiful-subarrays/solutions/3286372/java-c-python-prefix-xor/
        import collections
        ans = prefix = 0
        freq = collections.Counter({prefix: 1})
        for num in nums:
            prefix ^= num
            ans += freq[prefix]  # prefix is seen freq[prefix] times previously, which indicates that there are freq[prefix] indices such that the XOR of nums[i] to num equals to 0, where 0 <= i <= (current index) for each index i
            freq[prefix] += 1
        return ans
