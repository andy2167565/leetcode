class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        import collections
        counter = collections.Counter(nums)
        mx = max(counter.values())
        return sum(filter(lambda x: x == mx, counter.values()))
