# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
#======== <Solution 1> ========#
        self.mirror(root.left)  # Mirror one of the child
        return self.isSameTree(root.left, root.right)  # Compare two children to see if they are the same

    def mirror(self, node):
        if node:
            node.left, node.right = node.right, node.left
            self.mirror(node.left)
            self.mirror(node.right)

    def isSameTree(self, p, q):
        if not p or not q:
            return p == q
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

#======== <Solution 2> ========#
        return self.isMirror(root.left, root.right)

    def isMirror(self, node1, node2):
        if node1 and node2 and node1.val == node2.val:
            return self.isMirror(node1.left, node2.right) and self.isMirror(node1.right, node2.left)
        return node1 == node2

#======== <Solution 3> ========#
        stack = [(root.left, root.right)]
        while stack:
            l, r = stack.pop()
            if l and r and l.val == r.val:
                stack.extend([(l.left, r.right), (l.right, r.left)])
            elif l or r:
                return False
        return True
