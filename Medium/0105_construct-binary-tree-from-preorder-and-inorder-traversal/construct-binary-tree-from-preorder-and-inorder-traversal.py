# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Reference 1: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/discuss/34579/Python-short-recursive-solution./32947
        # Reference 2: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/discuss/2279180/PYTHON-or-EXPLAINED-oror
        if inorder:
            ind = inorder.index(preorder.pop(0))  # First value of preorder must be root
            root = TreeNode(inorder[ind])
            root.left = self.buildTree(preorder, inorder[0:ind])  # Start from left subtree
            root.right = self.buildTree(preorder, inorder[ind + 1:])
            return root
