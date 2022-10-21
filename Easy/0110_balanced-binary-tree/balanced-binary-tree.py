# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
#======== <Solution 1> ========#
        height, balanced = self.getResult(root)
        return balanced
    
    def getResult(self, node):
        if not node: return 0, True
        l_height, l_balanced = self.getResult(node.left)
        r_height, r_balanced = self.getResult(node.right)
        return max(l_height, r_height) + 1, l_balanced and r_balanced and abs(l_height - r_height) <= 1

#======== <Solution 2> ========#
        # Output = actual height + 1
        if not root: return 1
        l_height, r_height = self.isBalanced(root.left), self.isBalanced(root.right)
        return l_height and r_height and abs(l_height - r_height) <= 1 and max(l_height, r_height) + 1

#======== <Solution 3> ========#
        if not root: return True
        return self.isBalanced(root.left) and self.isBalanced(root.right) and abs(self.getDepth(root.left) - self.getDepth(root.right)) <= 1
    
    def getDepth(self, node):
        if not node: return 0
        return max(self.getDepth(node.left), self.getDepth(node.right)) + 1
