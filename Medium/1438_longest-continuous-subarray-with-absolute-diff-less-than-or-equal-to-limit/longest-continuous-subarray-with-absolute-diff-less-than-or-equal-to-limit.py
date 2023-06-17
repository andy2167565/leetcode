class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
# Reference: https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/solutions/609771/java-c-python-deques-o-n/
#======== <Solution 1> ========#
        import bisect
        l, arr = 0, []
        for r in range(len(nums)):
            bisect.insort(arr, nums[r])  # Keep an increasing list
            if arr[-1] - arr[0] > limit:  # Move the sliding window
                arr.pop(bisect.bisect(arr, nums[l]) - 1)
                l += 1
        return r - l + 1

#======== <Solution 2> ========#
        import heapq
        maxHeap, minHeap = [], []
        ans = l = 0
        for r, num in enumerate(nums):
            heapq.heappush(maxHeap, [-num, r])
            heapq.heappush(minHeap, [num, r])
            while abs(maxHeap[0][0]) - minHeap[0][0] > limit:
                l = min(maxHeap[0][1], minHeap[0][1]) + 1
                while maxHeap[0][1] < l:
                    heapq.heappop(maxHeap)
                while minHeap[0][1] < l:
                    heapq.heappop(minHeap)
            ans = max(ans, r - l + 1)
        return ans

#======== <Solution 3> ========#
        import collections
        i, maxQueue, minQueue = 0, collections.deque(), collections.deque()
        for num in nums:
            while len(maxQueue) and num > maxQueue[-1]:
                maxQueue.pop()
            while len(minQueue) and num < minQueue[-1]:
                minQueue.pop()
            maxQueue.append(num)
            minQueue.append(num)
            if maxQueue[0] - minQueue[0] > limit:
                if maxQueue[0] == nums[i]:
                    maxQueue.popleft()
                if minQueue[0] == nums[i]:
                    minQueue.popleft()
                i += 1
        return len(nums) - i
