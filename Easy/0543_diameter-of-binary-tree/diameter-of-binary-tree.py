# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Reference 1: https://leetcode.com/problems/diameter-of-binary-tree/discuss/1539484/EASY-TRICK-INTERVIEWERS-DON'T-WANT-YOU-TO-KNOW!
        # Reference 2: https://leetcode.com/problems/diameter-of-binary-tree/discuss/1515564/Python-Easy-to-understand-solution-w-Explanation
        self.diameter = 0
        def height(node):
            if not node: return -1  # Define the height of an empty tree to be -1 so that the final output, i.e total height of the tree, would be correct
            left_height, right_height = height(node.left), height(node.right)
            self.diameter = max(self.diameter, left_height + right_height + 2)  # The additional 2 accounts for the edge on the left plus the edge on the right since we define height = -1 when the node is empty
            return max(left_height, right_height) + 1
        height(root)
        return self.diameter
