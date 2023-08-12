# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        import collections
        graph, stack = collections.defaultdict(list), [(root, None)]
        while stack:  # Store connections between nodes and all their adjacent nodes
            node, parent = stack.pop()
            if parent:
                graph[parent.val].append(node.val)
                graph[node.val].append(parent.val)
            if node.left:
                stack.append((node.left, node))
            if node.right:
                stack.append((node.right, node))
        ans, seen, queue = -1, {start}, collections.deque([start])
        while queue:  # Start the infection
            for _ in range(len(queue)):
                node = queue.popleft()
                for adj in graph[node]:
                    if adj not in seen:
                        seen.add(adj)
                        queue.append(adj)
            ans += 1
        return ans
