class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        import collections
        ans = 0
        for num, count in collections.Counter(nums).items():
            if count > 1:
                ans ^= num
        return ans
