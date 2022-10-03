class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
#======== <Solution 1> ========#
        # Reference 1: https://leetcode.com/problems/maximum-sum-circular-subarray/discuss/178422/One-Pass
        # Reference 2: https://leetcode.com/problems/maximum-sum-circular-subarray/discuss/633058/Java-or-C%2B%2B-or-Python3-or-With-detailed-explanation-or-O(N)-time-or-O(1)
        curMax = curMin = maxSum = minSum = nums[0]
        for num in nums[1:]:
            curMax = max(curMax + num, num)
            maxSum = max(maxSum, curMax)
            curMin = min(curMin + num, num)
            minSum = min(minSum, curMin)
        return max(maxSum, sum(nums) - minSum) if maxSum > 0 else maxSum

#======== <Solution 2> ========#
        max_dp = [i for i in nums]
        min_dp = [i for i in nums]
        for i in range(1, len(nums)):
            if max_dp[i - 1] > 0:
                max_dp[i] += max_dp[i - 1]
            if min_dp[i - 1] < 0:
                min_dp[i] += min_dp[i - 1]
        return max(max(max_dp), sum(nums) - min(min_dp)) if max(nums) > 0 else max(nums)

# Reference: https://leetcode.com/problems/maximum-sum-circular-subarray/discuss/1348545/Python-3-solutions-Clean-and-Concise-O(1)-Space
#======== <Solution 3> ========#
        import heapq
        minHeap = [(0, -1)]  # (curSum, index)
        n, curSum, maxSum = len(nums), 0, nums[0]
        for i in range(2 * n):
            curSum += nums[i % n]
            while minHeap and i - minHeap[0][1] > n:  # Remove if the index of minHeap.top() is out of range size `n`
                heapq.heappop(minHeap)
            maxSum = max(maxSum, curSum - minHeap[0][0])
            heapq.heappush(minHeap, (curSum, i))
        return maxSum

#======== <Solution 4> ========#
        import collections
        dq = collections.deque([(0, -1)])  # (curSum, index), dq is an increasing queue
        n, curSum, maxSum = len(nums), 0, nums[0]
        for i in range(2 * n):
            curSum += nums[i % n]
            while dq and i - dq[0][1] > n:  # Remove if index of dq.front() is out of range size `n`
                dq.popleft()
            maxSum = max(maxSum, curSum - dq[0][0])  # Get the minimum preSum from the front of the deque
            while dq and dq[-1][0] >= curSum:  # We want to keep smaller preSums and the latest `curSum` is smaller which is better than old ones, don't need to keep those old values
                dq.pop()
            dq.append((curSum, i))
        return maxSum
