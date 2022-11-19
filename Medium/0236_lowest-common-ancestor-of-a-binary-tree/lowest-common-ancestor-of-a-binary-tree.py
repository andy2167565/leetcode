# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
#======== <Solution 1> ========#
        # Reference: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/discuss/65225/4-lines-C%2B%2BJavaPythonRuby
        if root in (None, p, q): return root
        l = self.lowestCommonAncestor(root.left, p, q)  # Find p or q in left subtree
        r = self.lowestCommonAncestor(root.right, p, q)  # Find p or q in right subtree
        return root if l and r else l or r  # Current node is LCA if p and q are found in left and right subtree respectively. Otherwise LCA is the node which is returned from either subtree.

#======== <Solution 2> ========#
        import collections
        stack, parent = collections.deque([root]), {root: None}
        while p not in parent or q not in parent:  # Keep updating stack until both p and q are included in parent
            node = stack.popleft()
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)
        ancestors = set()
        while p:  # Collect all ancestors of p
            ancestors.add(p)
            p = parent[p]
        while q not in ancestors:  # Travel through all ancestors of q and return the first one that appears in p's ancestors
            q = parent[q]
        return q
