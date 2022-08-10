# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
#======== <Recursive Solution> ========#
        if not root:
            return 0
        
        l_height = self.minDepth(root.left)
        r_height = self.minDepth(root.right)
        
        if l_height > 0 and r_height > 0:
            return min(l_height, r_height) + 1
        elif l_height > 0:
            return l_height + 1
        else:
            return r_height + 1
        
#======== <Iterative Solution> ========#
        if not root:
            return 0
        
        queue = [(root, 1)]
        while queue:
            node, depth = queue.pop(0)
            if not node:
                continue
            
            if not node.left and not node.right:
                return depth
            
            queue.append((node.left, depth + 1))
            queue.append((node.right, depth + 1))
