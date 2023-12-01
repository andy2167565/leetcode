# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def splitBST(self, root: Optional[TreeNode], target: int) -> List[Optional[TreeNode]]:
        if not root:
            return [None, None]
        if root.val > target:
            left_subtree, root.left = self.splitBST(root.left, target)
            return [left_subtree, root]
        root.right, right_subtree = self.splitBST(root.right, target)
        return [root, right_subtree]
