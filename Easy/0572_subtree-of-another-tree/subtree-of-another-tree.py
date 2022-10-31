# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
#======== <Solution 1> ========#
        if root: return self.isSameTree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, p, q):
        if not p or not q:
            return p == q
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

#======== <Solution 2> ========#
        return self.convertToString(subRoot) in self.convertToString(root)

    def convertToString(self, node):
        if node: return f'^{node.val}{self.convertToString(node.left)}{self.convertToString(node.right)}'
