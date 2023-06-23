# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
#======== <Solution 1> ========#
        import collections, heapq
        def traverse(node, row, col):  # Store node values and their corresponding row for each column
            if node:
                hashmap[col].append((row, node.val))
                traverse(node.left, row + 1, col - 1)
                traverse(node.right, row + 1, col + 1)
        ans, minHeap, hashmap = [], [], collections.defaultdict(list)
        traverse(root, 0, 0)
        for col, arr in hashmap.items():
            heapq.heappush(minHeap, (col, sorted(arr)))  # Sort by column, row, and value
        while minHeap:
            ans.append([value for _, value in heapq.heappop(minHeap)[1]])
        return ans

#======== <Solution 2> ========#
        import collections
        queue, hashmap = collections.deque([(root, 0, 0)]), collections.defaultdict(list)
        while queue:
            node, row, col = queue.popleft()
            hashmap[col].append((row, node.val))
            if node.left:
                queue.append((node.left, row + 1, col - 1))
            if node.right:
                queue.append((node.right, row + 1, col + 1))
        return [[value for _, value in sorted(arr)] for _, arr in sorted(hashmap.items())]
