# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        import collections
        def countSwaps(values):
            val_idx = {value: i for i, value in enumerate(sorted(values))}  # Sort the values in increasing order and assign the correct indices
            visited, swaps = [False] * len(values), 0
            for i in range(len(values)):
                count = 0
                while not visited[i] and i != val_idx[values[i]]:  # The position of values[i] is not correct
                    visited[i], i = True, val_idx[values[i]]
                    count += 1  # Count the number of incorrect nodes
                swaps += max(0, count - 1)  # Only need (count - 1) swaps for count nodes
            return swaps
        queue, ans = collections.deque([root]), 0
        while queue:
            values = []
            for _ in range(len(queue)):
                node = queue.popleft()
                values.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans += countSwaps(values)
        return ans
