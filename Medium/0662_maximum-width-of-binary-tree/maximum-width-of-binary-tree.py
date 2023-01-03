# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
#======== <Solution 1> ========#
        import collections
        width, level = 0, collections.deque([(1, root)])  # Assign an ordered index to each node for width calculation. Null is considered as well.
        while level:
            width = max(width, level[-1][0] - level[0][0] + 1)
            for _ in range(len(level)):
                index, node = level.popleft()
                if node.left:
                    level.append((index * 2, node.left))
                if node.right:
                    level.append((index * 2 + 1, node.right))
        return width

#======== <Solution 2> ========#
        width, level = 0, [(1, root)]
        while level:
            width = max(width, level[-1][0] - level[0][0] + 1)
            level = [child for index, node in level for child in enumerate((node.left, node.right), 2 * index) if child[1]]
        return width

#======== <Solution 3> ========#
        import collections
        d = collections.defaultdict(list)
        def dfs(node, level, col):  # col is the index of node in each level starting from left
            if node:
                d[level].append(col)  # Collect all cols as a list for each level
                dfs(node.left, level + 1, col * 2)
                dfs(node.right, level + 1, col * 2 + 1)
        return dfs(root, 0, 0) or max(d[level][-1] - d[level][0] + 1 for level in d)  # Calculate max width for each level and pick the largest one
