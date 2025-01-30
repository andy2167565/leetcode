class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        return len(set(int(str(num)[::-1]) for num in nums).union(set(nums)))
