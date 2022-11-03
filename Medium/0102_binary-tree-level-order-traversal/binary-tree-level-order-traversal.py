# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#======== <Solution 1> ========#
        # Reference: https://leetcode.com/problems/binary-tree-level-order-traversal/discuss/33464/5-6-lines-fast-python-solution-(48-ms)
        ans, level = [], [root]
        while root and level:
            ans.append([node.val for node in level])
            level = [leaf for node in level for leaf in (node.left, node.right) if leaf]
        return ans

#======== <Solution 2> ========#
        # Reference 1: https://leetcode.com/problems/binary-tree-level-order-traversal/discuss/1219328/JS-Python-Java-C%2B%2B-or-Easy-BFS-Queue-Solution-w-Explanation
        # Reference 2: https://leetcode.com/problems/binary-tree-level-order-traversal/discuss/1219538/Python-Simple-bfs-explained
        import collections
        queue, ans = collections.deque([root]), []
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                if node:
                    level.append(node.val)
                    queue.extend([node.left, node.right])
            if level:
                ans.append(level)
        return ans

#======== <Solution 3> ========#
        # Reference: https://leetcode.com/problems/binary-tree-level-order-traversal/discuss/33550/Python-Solution-with-Detailed-Explanation
        ans = []
        self.dfs(root, 0, ans)
        return ans

    def dfs(self, root, level, ans):
        if root:
            if len(ans) <= level:
                ans.append([])
            ans[level].append(root.val)
            self.dfs(root.left, level + 1, ans)
            self.dfs(root.right, level + 1, ans)
