class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        import collections
        for num, count in sorted(collections.Counter(nums).items(), reverse=True):
            if count == 1:
                return num
        return -1
