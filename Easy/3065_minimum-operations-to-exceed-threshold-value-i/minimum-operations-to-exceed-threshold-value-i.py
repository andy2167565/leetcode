class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        import bisect
        return bisect.bisect_left(sorted(nums), k)
