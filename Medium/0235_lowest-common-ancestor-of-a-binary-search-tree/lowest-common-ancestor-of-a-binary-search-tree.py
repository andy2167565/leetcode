# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
#======== <Solution 1> ========#
        # Reference: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/discuss/1347857/C%2B%2BJavaPython-Iterate-in-BST-Picture-explain-Time%3A-O(H)-Space%3A-O(1)
        small, large = min(p.val, q.val), max(p.val, q.val)
        while root:
            if root.val > large:  # p, q belong to the left subtree
                root = root.left
            elif root.val < small:  # p, q belong to the right subtree
                root = root.right
            else:  # small <= root.val <= large -> root is the LCA between p and q
                return root

#======== <Solution 2> ========#
        if root.val > max(p.val, q.val):
            return self.lowestCommonAncestor(root.left, p, q)
        if root.val < min(p.val, q.val):
            return self.lowestCommonAncestor(root.right, p, q)
        return root  # min(p.val, q.val) < root.val < max(p.val, q.val)

# Reference: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/discuss/64963/3-lines-with-O(1)-space-1-Liners-Alternatives
#======== <Solution 3> ========#
        while (root.val - p.val) * (root.val - q.val) > 0:
            root = (root.left, root.right)[p.val > root.val]
        return root

#======== <Solution 4> ========#
        next = (p.val < root.val > q.val and root.left) or (p.val > root.val < q.val and root.right)
        return self.lowestCommonAncestor(next, p, q) if next else root
