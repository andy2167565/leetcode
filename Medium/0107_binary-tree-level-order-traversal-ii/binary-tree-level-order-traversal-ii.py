# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
#======== <Iterative Solution 1>: Use List as Queue ========#
        if not root:
            return []
        result = []
        cur_level = []
        # Use None to separate each level
        queue = [root, None]
        while queue:
            node = queue.pop(0)
            if node:
                # Collect node values in current level
                cur_level.append(node.val)
                # Append nodes in next level if exist
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            else:
                if cur_level:
                    # Add node values in current level to result list
                    result.insert(0, cur_level)
                    cur_level = []
                    # Use None to separate each level
                    queue.append(None)
        return result
        
#======== <Iterative Solution 2> ========#
        if not root:
            return []
        result = []
        cur_level = [root]
        while cur_level:
            # Add node values in current level to result list
            result.insert(0, [node.val for node in cur_level])
            # Generate node list of next level
            next_level = []
            for node in cur_level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            cur_level = next_level
        return result
