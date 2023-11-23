# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        # Reference: https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/solutions/1612105/3-steps/
        def find(node, val, path) -> bool:
            if node.val == val:  # Reach the target node
                return True
            if node.left and find(node.left, val, path):
                path += 'L'
            elif node.right and find(node.right, val, path):
                path += 'R'
            return path
        start_path, dest_path = [], []
        find(root, startValue, start_path)  # Find the path from startValue to root
        find(root, destValue, dest_path)  # Find the path from destValue to root
        while len(start_path) and len(dest_path) and start_path[-1] == dest_path[-1]:  # Remove common prefix path
            start_path.pop()
            dest_path.pop()
        return ''.join('U' * len(start_path)) + ''.join(reversed(dest_path))  # Replace all steps in the start direction to 'U' and add destination direction
