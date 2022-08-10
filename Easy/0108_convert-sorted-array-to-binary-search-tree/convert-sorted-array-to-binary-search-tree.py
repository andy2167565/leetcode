# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
#======== <Recursive Solution 1> ========#
        return self.recursive(nums, 0, len(nums)-1)
    
    def recursive(self, nums, start, end):
        # Divide-and-conquer
        if start <= end:
            # Conquer
            mid = (start + end) // 2
            node = TreeNode(nums[mid])
            # Divide
            node.left = self.recursive(nums, start, mid-1)
            node.right = self.recursive(nums, mid+1, end)
            return node
        
#======== <Recursive Solution 2> ========#
        if not nums:
            return None
        
        # Divide-and-conquer
        # Conquer
        mid = len(nums) // 2
        node = TreeNode(nums[mid])
        # Divide
        node.left = self.sortedArrayToBST(nums[:mid])
        node.right = self.sortedArrayToBST(nums[mid+1:])
        return node
