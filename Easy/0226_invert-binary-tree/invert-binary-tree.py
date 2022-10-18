# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
# Reference: https://leetcode.com/problems/invert-binary-tree/discuss/62714/3-4-lines-Python
#======== <Solution 1> ========#
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
            return root

#======== <Solution 2> ========#
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                node.left, node.right = node.right, node.left
                stack += node.left, node.right
        return root
