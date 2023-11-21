class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        # Reference: https://leetcode.com/problems/find-the-most-competitive-subsequence/solutions/952786/java-c-python-one-pass-stack-solution/
        stack = []
        for i, num in enumerate(nums):
            while stack and stack[-1] > num and len(stack) - 1 + len(nums) - i >= k:  # Check if there are enough elements to append
                stack.pop()
            if len(stack) < k:
                stack.append(num)
        return stack
