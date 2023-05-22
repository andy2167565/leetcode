class Solution:
    def minDifference(self, nums: List[int]) -> int:
# Reference: https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/solutions/730567/java-c-python-straight-forward/
#======== <Solution 1> ========#
        nums.sort()
        return min(M - m for m, M in zip(nums[:4], nums[-4:]))

#======== <Solution 2> ========#
        import heapq
        return min(M - m for M, m in zip(heapq.nlargest(4, nums), heapq.nsmallest(4, nums)[::-1]))
