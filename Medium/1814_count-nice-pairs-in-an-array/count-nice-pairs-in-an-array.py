class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        import collections
        freqs = collections.Counter(num - int(str(num)[::-1]) for num in nums)  # nums[i] - rev(nums[i]) == nums[j] - rev(nums[j])
        return sum(freq * (freq - 1) // 2 for freq in freqs.values()) % (10**9 + 7)
