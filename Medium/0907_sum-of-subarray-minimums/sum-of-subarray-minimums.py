class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        # Reference: https://leetcode.com/problems/sum-of-subarray-minimums/solutions/257811/python-o-n-slightly-easier-to-grasp-solution-explained/
        arr = [0] + arr  # Add zeros to arr and stack to avoid dealing with empty stack
        stack, mins = [0], [0] * len(arr)  # mins[i]: Sum of minimums of subarrays ending with arr[i - 1]
        for i in range(len(arr)):
            while arr[stack[-1]] > arr[i]:  # New local minimum
                stack.pop()
            j = stack[-1]
            mins[i] = mins[j] + (i - j) * arr[i]
            stack.append(i)
        return sum(mins) % (10**9 + 7)
