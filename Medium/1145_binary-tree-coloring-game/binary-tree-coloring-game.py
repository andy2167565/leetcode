# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:
        c = [0, 0]  # The counts of left and right subtrees of root x
        def count(node):  # Count the subtrees with node as root
            if not node:
                return 0
            l, r = count(node.left), count(node.right)
            if node.val == x:
                c[0], c[1] = l, r
            return l + r + 1
        return count(root) // 2 < max(max(c), n - sum(c) - 1)  # Check if any of the subtrees that player 2 can possibly get is more than half of the nodes n
