# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
#======== <Solution 1> ========#
        def subtreeSum(root):
            if not root:
                return 0
            curr_sum = subtreeSum(root.left) + subtreeSum(root.right) + root.val
            subtree_sums.append(curr_sum)
            return curr_sum
        subtree_sums = []
        total_sum = subtreeSum(root)
        return max(curr_sum * (total_sum - curr_sum) for curr_sum in subtree_sums) % (10**9 + 7)

#======== <Solution 2> ========#
        def subtreeSum(root):
            if not root:
                return 0
            curr_sum = subtreeSum(root.left) + subtreeSum(root.right) + root.val
            self.ans = max(self.ans, curr_sum * (total_sum - curr_sum))
            return curr_sum
        self.ans = total_sum = 0
        total_sum = subtreeSum(root)  # Get total sum in first pass
        subtreeSum(root)  # Calculate the maximum product
        return self.ans % (10**9 + 7)
