# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
#======== <Solution 1> ========#
        import collections
        ans = []
        if root:
            level = collections.deque([root])
            while level:
                ans.append(level[-1].val)  # Append last value in each level
                for _ in range(len(level)):
                    node = level.popleft()
                    if node.left:
                        level.append(node.left)
                    if node.right:
                        level.append(node.right)
        return ans

# Reference: https://leetcode.com/problems/binary-tree-right-side-view/discuss/56064/5-9-Lines-Python-48%2B-ms
#======== <Solution 2> ========#
        ans = []
        if root:
            level = [root]
            while level:
                ans.append(level[-1].val)
                level = [kid for node in level for kid in (node.left, node.right) if kid]
        return ans

#======== <Solution 3> ========#
        def dfs(node, level, ans):
            if node:
                if level == len(ans):  # Add values whenever we first reach a new record level
                    ans.append(node.val)
                dfs(node.right, level + 1, ans)  # Starting from right node
                dfs(node.left, level + 1, ans)
            return ans
        return dfs(root, 0, [])

#======== <Solution 4> ========#
        if not root:
            return []
        r = self.rightSideView(root.right)
        l = self.rightSideView(root.left)
        return [root.val] + r + l[len(r):]  # If r ends earlier than l, continue with l starting from index len(r)
