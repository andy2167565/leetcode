# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if not n % 2:
            return []
        def dfs(n):
            if n not in memo:
                arr = []
                for i in range(1, n - 1, 2):
                    for l in dfs(i):
                        for r in dfs(n - i - 1):
                            arr.append(TreeNode(0, l, r))
                memo[n] = arr
            return memo[n]
        memo = {1: [TreeNode(0)]}
        return dfs(n)
