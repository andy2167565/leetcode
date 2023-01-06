# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
#======== <Solution 1> ========#
        # Reference: https://leetcode.com/problems/inorder-successor-in-bst/solutions/72656/java-python-solution-o-h-time-and-o-1-space-iterative/
        successor = None
        while root:
            if p.val < root.val:
                successor, root = root, root.left
            else:
                root = root.right
        return successor

#======== <Solution 2> ========#
        sortedBST = self.inorder(root)
        for i, node in enumerate(sortedBST):
            if node == p:
                return None if i == len(sortedBST) - 1 else sortedBST[i + 1]

    def inorder(self, root):
        return self.inorder(root.left) + [root] + self.inorder(root.right) if root else []

#======== <Solution 3> ========#
        if root:
            return self.inorderSuccessor(root.left, p) or root if p.val < root.val else self.inorderSuccessor(root.right, p)
