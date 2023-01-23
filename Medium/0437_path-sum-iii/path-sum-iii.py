# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # Reference 1: https://leetcode.com/problems/path-sum-iii/solutions/141424/python-step-by-step-walk-through-easy-to-understand-two-solutions-comparison/
        # Reference 2: https://leetcode.com/problems/path-sum-iii/solutions/91892/python-solution-with-detailed-explanation/
        self.ans = 0
        cache = {0: 1}  # Save the frequency of all the path sum from root to current node
        self.dfs(root, targetSum, 0, cache)
        return self.ans

    def dfs(self, root, targetSum, currSum, cache):
        if root:
            currSum += root.val  # Current path sum from root to current node
            self.ans += cache.get(currSum - targetSum, 0)  # There is a valid targetSum at the end of current path if the complement path sum between currSum and targetSum is already stored in cache
            cache[currSum] = cache.get(currSum, 0) + 1
            self.dfs(root.left, targetSum, currSum, cache)
            self.dfs(root.right, targetSum, currSum, cache)
            cache[currSum] -= 1  # Remove 1 currSum count when moving to a different branch to make sure that the number of complement paths returned always corresponds to paths that ended at a predecessor node
