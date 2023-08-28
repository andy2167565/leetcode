# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        i, stack = 0, [TreeNode(preorder[0])]
        for v in preorder[1:]:
            node = TreeNode(v)
            while stack[-1].val == postorder[i]:  # Move to the right subtree of the incomplete root
                stack.pop()
                i += 1
            if not stack[-1].left:
                stack[-1].left = node
            else:
                stack[-1].right = node
            stack.append(node)
        return stack[0]
