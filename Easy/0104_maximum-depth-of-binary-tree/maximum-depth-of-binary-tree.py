# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
#======== <Recursive Solution> ========#
        if not root:
            return 0
        else:
            return max(self.maxDepth(root.left)+1, self.maxDepth(root.right)+1)
        
#======== <Iterative Solution> ========#
        if not root:
            return 0
        stack = [(root, 1)]
        max_level = 0
        while stack:
            # Store the level for each node
            node, level = stack.pop()
            if node.left:
                stack.append((node.left, level+1))
            if node.right:
                stack.append((node.right, level+1))
            # Update maximum level in case it start counting nodes from lower level
            max_level = max(level, max_level)
        return max_level
