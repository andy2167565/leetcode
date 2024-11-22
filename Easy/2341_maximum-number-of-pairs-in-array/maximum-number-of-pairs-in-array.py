class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        import collections
        ans = (divmod(count, 2) for count in collections.Counter(nums).values())
        return list(map(sum, zip(*ans)))
