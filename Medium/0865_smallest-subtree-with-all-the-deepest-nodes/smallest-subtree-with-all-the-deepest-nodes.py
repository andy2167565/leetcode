# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
# This question is the same as 1123: https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/
# Reference: https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/solutions/334577/java-c-python-two-recursive-solution/
#======== <Solution 1> ========#
        # Reference: https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/solutions/146808/c-java-python-one-pass/
        def dfs(node):
            if not node:
                return None, 0
            left_lca, left_depth = dfs(node.left)
            right_lca, right_depth = dfs(node.right)
            if left_depth > right_depth:
                return left_lca, left_depth + 1
            if left_depth < right_depth:
                return right_lca, right_depth + 1
            return node, left_depth + 1  # Left node and right node have the same depth so return the parent of both nodes
        return dfs(root)[0]

#======== <Solution 2> ========#
        self.lca, self.deepest = None, 0
        def dfs(node, depth):
            self.deepest = max(self.deepest, depth)
            if not node:
                return depth
            left_depth, right_depth = dfs(node.left, depth + 1), dfs(node.right, depth + 1)
            if left_depth == right_depth == self.deepest:  # Update LCA when there is larger depth and the depths of left node and right node equal to it
                self.lca = node
            return max(left_depth, right_depth)
        dfs(root, 0)
        return self.lca
