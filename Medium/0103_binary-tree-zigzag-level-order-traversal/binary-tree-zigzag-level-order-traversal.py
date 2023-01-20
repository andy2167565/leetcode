# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
# Reference: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/solutions/749036/python-clean-bfs-solution-explained/
#======== <Solution 1> ========#
        if not root: return []
        import collections
        queue, ans, direction = collections.deque([root]), [], 1
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(level[::direction])
            direction *= -1
        return ans

#======== <Solution 2> ========#
        if not root: return []
        import collections
        queue, ans, even_level = collections.deque([root]), [], False
        while queue:
            level = collections.deque()
            for _ in range(len(queue)):
                node = queue.popleft()
                if even_level:
                    level.appendleft(node.val)
                else:
                    level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(list(level))
            even_level = not even_level
        return ans
