# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        children, val_node = set(), {}
        for parent, child, isLeft in descriptions:
            parent_node = val_node.setdefault(parent, TreeNode(parent))
            child_node = val_node.setdefault(child, TreeNode(child))
            if isLeft:
                parent_node.left = child_node
            else:
                parent_node.right = child_node
            children.add(child)
        root_val = (set(val_node) - children).pop()
        return val_node[root_val]
