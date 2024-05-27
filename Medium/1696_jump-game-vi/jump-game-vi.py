class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        # Reference: https://leetcode.com/problems/jump-game-vi/solutions/1260843/c-java-python-dp-decreasing-deque-clean-concise-time-o-n-space-o-k/
        import collections
        dq = collections.deque([0])  # Store index of nums elements, elements is in decreasing order and the front is the maximum element
        for i in range(1, len(nums)):
            nums[i] = nums[dq[0]] + nums[i]  # nums[i] = max(nums[i - k], nums[i - k + 1],..., nums[i - 1]) + nums[i] = nums[dq.front()] + nums[i]
            while dq and nums[dq[-1]] <= nums[i]:  # Eliminate elements less than or equal to nums[i], which will never be chosen in the future
                dq.pop()
            dq.append(i)  # Add a nums[i] to the dq
            if i - dq[0] >= k:  # The last element is out of window size k
                dq.popleft()
        return nums[-1]
