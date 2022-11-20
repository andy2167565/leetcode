# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        sortedBST = []
        self.inorder(root, sortedBST)  # Convert the tree into a sorted array
        answer = []
        for query in queries:  # Apply binary search on sorted array for each query
            idx = self.binarySearch(sortedBST, query)
            if sortedBST[idx] == query:
                mini = maxi = sortedBST[idx]
            elif sortedBST[idx] > query:
                mini = sortedBST[idx - 1] if idx else -1
                maxi = sortedBST[idx]
            else:
                mini = sortedBST[idx]
                maxi = sortedBST[idx + 1] if idx < len(sortedBST) - 1 else -1
            answer.append([mini, maxi])
        return answer

    def inorder(self, root, arr):
        if root:
            self.inorder(root.left, arr)
            arr.append(root.val)
            self.inorder(root.right, arr)

    def binarySearch(self, nums, target):
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid
        return l
