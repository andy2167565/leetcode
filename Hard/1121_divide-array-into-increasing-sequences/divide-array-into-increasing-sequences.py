class Solution:
    def canDivideIntoSubsequences(self, nums: List[int], k: int) -> bool:
        # Reference: https://leetcode.com/problems/divide-array-into-increasing-sequences/solutions/334111/java-c-python-one-pass-o-1-space-and-prove/
        import collections
        return k * max(collections.Counter(nums).values()) <= len(nums)
