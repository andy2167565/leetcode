# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
# Reference: https://leetcode.com/problems/validate-binary-search-tree/discuss/786520/General-Tree-Traversal-Problems-interview-Prep
#======== <Solution 1> ========#
        sortedBST = self.inorder(root)
        return all(sortedBST[i - 1] < sortedBST[i] for i in range(1, len(sortedBST)))

    def inorder(self, root):
        if not root: return []
        return self.inorder(root.left) + [root.val] + self.inorder(root.right)

#======== <Solution 2> ========#
        # Reference 1: https://leetcode.com/problems/validate-binary-search-tree/discuss/32178/Clean-Python-Solution/359312
        # Reference 2: https://leetcode.com/problems/validate-binary-search-tree/discuss/146601/Python3-100-using-easy-recursion
        return self.checkBST(root, float('-inf'), float('inf'))

    def checkBST(self, root, l, r):
        return not root or l < root.val < r and self.checkBST(root.left, l, root.val) and self.checkBST(root.right, root.val, r)

#======== <Solution 3> ========#
        stack = [(root, float('-inf'), float('inf'))]
        while stack:
            node, l, r = stack.pop()
            if not l < node.val < r:
                return False
            if node.left:
                stack.append((node.left, l, node.val))
            if node.right:
                stack.append((node.right, node.val, r))
        return True
