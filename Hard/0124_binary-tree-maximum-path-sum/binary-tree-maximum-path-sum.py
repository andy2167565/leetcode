# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Reference: https://leetcode.com/problems/binary-tree-maximum-path-sum/solutions/603423/python-recursion-stack-thinking-process-diagram/
        def dfs(node):
            if not node: return 0
            # Only add positive gains
            left_gain = max(dfs(node.left), 0)
            right_gain = max(dfs(node.right), 0)
            self.max_sum = max(self.max_sum, node.val + left_gain + right_gain)  # Update max_sum
            return node.val + max(left_gain, right_gain)  # Only choose branch with greater path sum for parent
        self.max_sum = float('-inf')
        dfs(root)
        return self.max_sum
