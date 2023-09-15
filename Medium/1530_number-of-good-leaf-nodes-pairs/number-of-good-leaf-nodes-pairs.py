# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        # Reference: https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/solutions/755767/python-postorder-traversal/
        self.count = 0
        def dfs(node):
            if not node:
                return []
            if not node.left and not node.right:
                return [1]
            l_counts, r_counts = dfs(node.left), dfs(node.right)
            self.count += sum(l + r <= distance for l in l_counts for r in r_counts)  # Calculate the distances between leaves from left tree and right tree with node as LCA
            return [n + 1 for n in l_counts + r_counts if n + 1 < distance]
        dfs(root)
        return self.count
