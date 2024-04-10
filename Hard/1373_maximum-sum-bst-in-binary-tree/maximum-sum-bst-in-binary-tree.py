# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        # Reference: https://leetcode.com/problems/maximum-sum-bst-in-binary-tree/solutions/531800/python-easy-traversal-with-explanation/
        self.ans = 0
        def traverse(node):
            if not node:
                return 0, True, float('inf'), float('-inf')
            sum1, bst1, min1, max1 = traverse(node.left)
            sum2, bst2, min2, max2 = traverse(node.right)
            if bst1 and bst2 and max1 < node.val < min2:
                curr_sum = node.val + sum1 + sum2
                self.ans = max(self.ans, curr_sum)
                return curr_sum, True, min(min1, node.val), max(max2, node.val)
            return 0, False, float('inf'), float('-inf')
        traverse(root)
        return self.ans
