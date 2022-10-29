# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
#======== <Solution 1> ========#
        return self.buildBST(nums, 0, len(nums) - 1)

    def buildBST(self, nums, start, end):
        if start <= end:
            mid = (start + end) // 2  # mid will be left of two middle elements in even length array
            return TreeNode(nums[mid], self.buildBST(nums, start, mid - 1), self.buildBST(nums, mid + 1, end))

#======== <Solution 2> ========#
        if not nums: return None
        mid = len(nums) // 2  # mid will be right of two middle elements in even length array
        return TreeNode(nums[mid], self.sortedArrayToBST(nums[:mid]), self.sortedArrayToBST(nums[mid + 1:]))
