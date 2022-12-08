# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
#======== <Solution 1> ========#
        def dfs(node):
            if not node: return []
            return dfs(node.left) + [node.val] + dfs(node.right)
        BSTList = dfs(root)
        return BSTList[k - 1]

#======== <Solution 2> ========#
        import collections
        dq = collections.deque(maxlen=k)
        while True:
            while root:
                dq.append(root)
                root = root.left
            root = dq.pop()
            if k == 1:
                return root.val
            k -= 1
            root = root.right
