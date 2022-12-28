# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
#======== <Solution 1> ========#
        ans = []
        self.dfs(root, targetSum, [], ans)
        return ans

    def dfs(self, root, targetSum, path, ans):
        if root:
            path.append(root.val)
            if not root.left and not root.right and root.val == targetSum:  # Found a valid root-to-leaf path
                ans.append(path.copy())  # Need to append a copy of path in backtracking
            self.dfs(root.left, targetSum - root.val, path, ans)
            self.dfs(root.right, targetSum - root.val, path, ans)
            path.pop()  # Backtracking

#======== <Solution 2> ========#
        if not root:
            return []
        if not root.left and not root.right and root.val == targetSum:
            return [[root.val]]
        child = self.pathSum(root.left, targetSum - root.val) + self.pathSum(root.right, targetSum - root.val)
        return [[root.val] + value for value in child]

#======== <Solution 3> ========#
        import collections
        ans = []
        if root:
            queue = collections.deque([(root, root.val, [root.val])])
            while queue:
                curr, value, path = queue.popleft()
                if not curr.left and not curr.right and value == targetSum:
                    ans.append(path)
                if curr.left:
                    queue.append((curr.left, value + curr.left.val, path + [curr.left.val]))
                if curr.right:
                    queue.append((curr.right, value + curr.right.val, path + [curr.right.val]))
        return ans

#======== <Solution 4> ========#
        ans = []
        if root:
            stack = [(root, targetSum - root.val, [root.val])]
            while stack:
                curr, value, path = stack.pop()
                if not curr.left and not curr.right and not value:
                    ans.append(path)
                if curr.right:
                    stack.append((curr.right, value - curr.right.val, path + [curr.right.val]))
                if curr.left:
                    stack.append((curr.left, value - curr.left.val, path + [curr.left.val]))
        return ans

#======== <Solution 5> ========#
        ans = []
        if root:
            stack = [(root, [root.val])]
            while stack:
                curr, path = stack.pop()
                if not curr.left and not curr.right and sum(path) == targetSum:
                    ans.append(path)
                if curr.right:
                    stack.append((curr.right, path + [curr.right.val]))
                if curr.left:
                    stack.append((curr.left, path + [curr.left.val]))
        return ans
