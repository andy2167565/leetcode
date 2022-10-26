# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
#======== <Solution 1> ========#
        if not root: return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

#======== <Solution 2> ========#
        if not root: return 0
        stack, max_level = [(root, 1)], 0
        while stack:
            node, level = stack.pop()  # Store the level for each node
            if node.left:
                stack.append((node.left, level + 1))
            if node.right:
                stack.append((node.right, level + 1))
            max_level = max(level, max_level)  # Update maximum level in case it start counting nodes from lower level
        return max_level
