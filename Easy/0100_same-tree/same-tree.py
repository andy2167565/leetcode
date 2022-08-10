# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
#======== <Recursive Solution 1> ========#
        if not p and not q:
            return True
        elif p and q:
            same_val = p.val == q.val
            same_left = self.isSameTree(p.left, q.left)
            same_right = self.isSameTree(p.right, q.right)
            return same_val and same_left and same_right
        else:
            return False
        
#======== <Recursive Solution 2> ========#
        if not p or not q:
            return p == q
        return (p.val == q.val) and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
#======== <Iterative Solution> ========#
        stack = [(p, q)]
        while stack:
            # Pop last pair from the stack
            l, r = stack.pop()
            if l and r:
                if l.val != r.val:
                    return False
                else:
                    stack.append((l.left, r.left))
                    stack.append((l.right, r.right))
            elif l or r:
                return False
        return True
