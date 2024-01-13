class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        import collections
        ans, counter = 0, collections.Counter(num % value for num in nums)
        while counter[ans % value]:
            counter[ans % value] -= 1
            ans += 1
        return ans
