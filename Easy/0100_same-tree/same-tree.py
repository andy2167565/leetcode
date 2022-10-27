# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
#======== <Solution 1> ========#
        if not p or not q:
            return p == q
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

#======== <Solution 2> ========#
        stack = [(p, q)]
        while stack:
            l, r = stack.pop()
            if l and r and l.val == r.val:
                stack.extend([(l.left, r.left), (l.right, r.right)])
            # Possible cases:
            # 1) l and r and l.val != r.val
            # 2) l or r
            # l == r only when both l and r are None
            elif l != r:
                return False
        return True
