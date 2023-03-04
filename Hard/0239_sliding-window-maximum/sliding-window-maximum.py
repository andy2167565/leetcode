class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Reference 1: https://leetcode.com/problems/sliding-window-maximum/solutions/871317/clear-thinking-process-with-picture-brute-force-to-mono-deque-python-java-javascript/
        # Reference 2: https://leetcode.com/problems/sliding-window-maximum/solutions/3231782/239-time-93-21-and-space-81-39-solution-with-step-by-step-explanation/
        import collections
        ans, window = [], collections.deque()  # Store the indices of the elements in the sliding window
        for i, num in enumerate(nums):
            if window and window[0] == i - k:  # Remove the first element if it is outside the window
                window.popleft()
            while window and nums[window[-1]] < num:  # Remove elements that are smaller than current element from the end of window so that the first element is maximum
                window.pop()
            window.append(i)
            if i >= k - 1:  # Append the maximum element in the window to ans
                ans.append(nums[window[0]])
        return ans
