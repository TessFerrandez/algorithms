'''
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.
'''
from TreeNode import TreeNode, deserialize


class Codec:
    def serialize(self, root):
        def dfs(node):
            if node:
                vals.append(str(node.val))
                dfs(node.left)
                dfs(node.right)
            else:
                vals.append('#')

        vals = []
        dfs(root)
        return ' '.join(vals)

    def deserialize(self, data):
        def dfs():
            val = next(vals)
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()
            return node

        vals = iter(data.split())
        return dfs()


serializer = Codec()
deserializer = Codec()
root = deserialize([1, 2, 3, None, None, 4, 5])
tree = deserializer.deserialize(serializer.serialize(root))
print("hello")
