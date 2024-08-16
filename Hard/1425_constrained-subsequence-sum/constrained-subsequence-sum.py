class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        # Reference: https://leetcode.com/problems/constrained-subsequence-sum/solutions/597751/java-c-python-o-n-decreasing-deque/
        import collections
        dq = collections.deque()
        for i in range(len(nums)):
            nums[i] += dq[0] if dq else 0  # dq[0]: The maximum result in the last element of results
            while len(dq) and nums[i] > dq[-1]:  # Keep dq decreasing
                dq.pop()
            if nums[i] > 0:
                dq.append(nums[i])
            if i >= k and dq and dq[0] == nums[i - k]:
                dq.popleft()
        return max(nums)  # Updated nums[i]: The maximum sum we can get if the last element is nums[i]
