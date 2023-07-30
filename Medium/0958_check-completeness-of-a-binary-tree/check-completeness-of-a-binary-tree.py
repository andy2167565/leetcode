# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
#======== <Solution 1> ========#
        import collections
        q = collections.deque([root])
        while q[0] is not None:
            node = q.popleft()
            q.append(node.left)
            q.append(node.right)
        return not any(q)

#======== <Solution 2> ========#
        def dfs(root, coord):
            if root:
                self.total += 1
                self.right_most = max(coord, self.right_most)
                dfs(root.left, 2 * coord)
                dfs(root.right, 2 * coord + 1)
        self.total = self.right_most = 0
        dfs(root, 1)
        return self.total == self.right_most
