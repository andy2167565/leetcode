# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
#======== <Recursive Solution 1> ========#
        if not root:
            return True
        # Mirror one of the child
        self.mirror(root.left)
        # Compare two children to see if they are the same
        return self.isSameTree(root.left, root.right)

    def mirror(self, node):
        if node:
            node.left, node.right = node.right, node.left
            self.mirror(node.left)
            self.mirror(node.right)

    def isSameTree(self, p, q):
        if not p or not q:
            return p == q
        return (p.val == q.val) and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
#======== <Recursive Solution 2> ========#
        if not root:
            return True
        return self.isMirror(root.left, root.right)
        
    def isMirror(self, node1, node2):
        if not node1 or not node2:
            return node1 == node2
        if node1.val != node2.val:
            return False
        return self.isMirror(node1.left, node2.right) and self.isMirror(node1.right, node2.left)
        
#======== <Iterative Solution> ========#
        if not root:
            return True
        stack = [(root.left, root.right)]
        while stack:
            l, r = stack.pop()
            if l and r:
                if l.val != r.val:
                    return False
                else:
                    stack.append((l.left, r.right))
                    stack.append((l.right, r.left))
            elif l or r:
                return False
        return True
