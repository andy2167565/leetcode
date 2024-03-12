class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        # Reference: https://leetcode.com/problems/minimum-absolute-difference-between-elements-with-constraint/solutions/3901622/heapq-or-union-find/
        import heapq
        right, left, ans = [], [], float('inf')
        for val, idx in sorted((val, idx) for idx, val in enumerate(nums)):
            heapq.heappush(right, (x + idx, val))
            heapq.heappush(left, (x - idx, val))
            while right and right[0][0] <= idx:
                ans = min(ans, val - heapq.heappop(right)[1])
            while left and left[0][0] <= -idx:
                ans = min(ans, val - heapq.heappop(left)[1])
        return ans
