# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
#======== <Solution 1> ========#
        import collections
        level_sum = collections.defaultdict(int)
        def levelSum(node, level):
            if node:
                level_sum[level] += node.val
                levelSum(node.left, level + 1)
                levelSum(node.right, level + 1)
        def cousinsSum(node, level, sibling):
            if node:
                node.val = level_sum[level] - node.val - sibling
                left_sibling = node.left.val if node.left else 0
                right_sibling = node.right.val if node.right else 0
                cousinsSum(node.left, level + 1, right_sibling)
                cousinsSum(node.right, level + 1, left_sibling)
        return levelSum(root, 0) or cousinsSum(root, 0, 0) or root

#======== <Solution 2> ========#
        root.val, curr_level = 0, [root]
        while curr_level:
            next_level, next_level_sum = [], 0
            for node in curr_level:  # Calculate the sum of next level
                for child in node.left, node.right:
                    if child:
                        next_level.append(child)
                        next_level_sum += child.val
            for node in curr_level:  # Consider the nodes at current level as parents
                cousins_sum = next_level_sum
                for child in node.left, node.right:  # Subtract the values of direct siblings
                    if child:
                        cousins_sum -= child.val
                for child in node.left, node.right:
                    if child:
                        child.val = cousins_sum
            curr_level = next_level
        return root
