# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        # <Recursive Solution>
        if not p and not q:
            return True
        elif p and q:
            return (p.val == q.val) and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False
        
        # <Iterative Solution>
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
