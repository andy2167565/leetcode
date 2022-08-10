# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
#======== <Recursive Solution 1> ========#
        if not root:
            return False
        # Reach leaf node that matches targetSum
        if not root.left and not root.right and root.val == targetSum:
            return True
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)
        
#======== <Recursive Solution 2> ========#
        if not root:
            return False
        
        targetSum -= root.val
        
        # Reach leaf node
        if not root.left and not root.right:
            # Match targetSum
            return targetSum == 0
        
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)
        
#======== <Iterative Solution> ========#
        if not root:
            return False
        
        queue = [root]
        while queue:
            node = queue.pop(0)
            if not node.left and not node.right:
                if node.val == targetSum:
                    return True
            if node.left:
                node.left.val += node.val
                queue.append(node.left)
            if node.right:
                node.right.val += node.val
                queue.append(node.right)
        return False
