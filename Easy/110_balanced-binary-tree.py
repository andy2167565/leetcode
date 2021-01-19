# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
#======== <Recursive Solution 1> ========#
        height, result = self.getResult(root)
        return result
    
    def getResult(self, node, balanced=True):
        if not node or not balanced:
            return 0, balanced

        l_height, balanced = self.getResult(node.left, balanced)
        r_height, balanced = self.getResult(node.right, balanced)

        if abs(l_height - r_height) > 1:
            balanced = False

        return max(l_height, r_height) + 1, balanced
        
#======== <Recursive Solution 2> ========#
        if not root: return 1
        l_height = self.isBalanced(root.left)
        if not l_height: return
        r_height = self.isBalanced(root.right)
        if not r_height: return
        return abs(l_height - r_height) <= 1 and max(l_height, r_height) + 1
        
#======== <Recursive Solution 3> ========#
        if not root:
            return True
        return abs(self.getDepth(root.left) - self.getDepth(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
    
    def getDepth(self, node):
        if not node:
            return 0
        return max(self.getDepth(node.left), self.getDepth(node.right)) + 1
