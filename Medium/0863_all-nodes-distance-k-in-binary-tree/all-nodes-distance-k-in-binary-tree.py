# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # Reference: https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/solutions/143729/python-dfs-and-bfs/
        import collections
        graph = collections.defaultdict(list)
        def dfs(parent, child):
            if parent and child:  # Build an undirected graph and assign child value for parent as the key and vice versa
                graph[parent.val].append(child.val)
                graph[child.val].append(parent.val)
            if child.left:
                dfs(child, child.left)
            if child.right:
                dfs(child, child.right)
        dfs(None, root)  # The initial parent node of the root is None
        bfs = [target.val]  # Start the breadth-first search from the target, hence the starting level is 0
        seen = set(bfs)
        for _ in range(k):  # All nodes at (k-1)th level must also be k steps away from the target node
            next_level = []
            for node in bfs:
                for neighbor in graph[node]:
                    if neighbor not in seen:
                        next_level.append(neighbor)
            bfs = next_level
            seen |= set(bfs)  # Add all the values in bfs into seen
        return bfs
