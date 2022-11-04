"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
#======== <Solution 1> ========#
        # Reference: https://leetcode.com/problems/clone-graph/discuss/1792858/Python3-ITERATIVE-BFS-(beats-98)-'less()greater''-Explained
        import collections
        if not node: return node
        q, clones = collections.deque([node]), {node.val: Node(node.val, [])}  # Map original node values to their clones
        while q:
            cur_node = q.popleft()
            for ngbr in cur_node.neighbors:
                if ngbr.val not in clones:  # Neighbor is not visited
                    clones[ngbr.val] = Node(ngbr.val, [])  # Store copy of the neighboring node
                    q.append(ngbr)
                clones[cur_node.val].neighbors.append(clones[ngbr.val])  # Connect the node copy at hand to its neighboring nodes (also copies)
        return clones[node.val]

#======== <Solution 2> ========#
        if not node: return node
        stack, clones = [node], {node.val: Node(node.val, [])}
        while stack:
            cur_node = stack.pop()
            for ngbr in cur_node.neighbors:
                if ngbr.val not in clones:
                    clones[ngbr.val] = Node(ngbr.val, [])
                    stack.append(ngbr)
                clones[cur_node.val].neighbors.append(clones[ngbr.val])
        return clones[node.val]

#======== <Solution 3> ========#
        if not node: return node
        clones = {node.val: Node(node.val, [])}
        self.dfs(node, clones)
        return clones[node.val]

    def dfs(self, cur_node, clones):
        for ngbr in cur_node.neighbors:
            if ngbr.val not in clones:
                clones[ngbr.val] = Node(ngbr.val, [])
                self.dfs(ngbr, clones)
            clones[cur_node.val].neighbors.append(clones[ngbr.val])
