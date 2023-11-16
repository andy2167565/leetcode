# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        import re
        vals = [(len(s[1]), int(s[2])) for s in re.findall('((-*)(\d+))', traversal)][::-1]  # (Depth, Node)
        def dfs(depth):
            if not vals or depth != vals[-1][0]:
                return None
            node = TreeNode(vals.pop()[1])
            node.left = dfs(depth + 1)
            node.right = dfs(depth + 1)
            return node
        return dfs(0)
