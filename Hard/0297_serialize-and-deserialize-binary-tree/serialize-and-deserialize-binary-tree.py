# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root: return '#'
        return ' '.join([str(root.val), self.serialize(root.left), self.serialize(root.right)])  # e.g. '1 2 # # 3 4 # # 5 # #'

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def dfs():
            val = next(vals)
            if val != '#':
                node = TreeNode(int(val))
                node.left = dfs()
                node.right = dfs()
                return node
        vals = iter(data.split())
        return dfs()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
