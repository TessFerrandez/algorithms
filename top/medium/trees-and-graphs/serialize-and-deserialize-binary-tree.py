from TreeNode import TreeNode


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
