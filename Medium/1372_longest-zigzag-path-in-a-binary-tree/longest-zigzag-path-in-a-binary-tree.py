# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return [-1, -1, -1]
            l, r = dfs(node.left), dfs(node.right)
            return [l[1] + 1, r[0] + 1, max(l[1] + 1, r[0] + 1, l[2], r[2])]  # [(max length in direction of node.left), (max length in direction of node.right), (max length in entire subtree)]
        return dfs(root)[-1]
