# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipMatchVoyage(self, root: Optional[TreeNode], voyage: List[int]) -> List[int]:
        ans, stack, i = [], [root], 0
        while stack:
            node = stack.pop()
            if node:
                if node and node.val != voyage[i]:
                    return [-1]
                i += 1
                if node.right and node.right.val == voyage[i]:
                    if node.left:
                        ans.append(node.val)
                    stack.extend([node.left, node.right])
                else:
                    stack.extend([node.right, node.left])
        return ans
