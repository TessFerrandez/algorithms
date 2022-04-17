from TreeNode import TreeNode, deserialize, arr_from_btree


class Solution:
    # using array
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def inorder(node):
            if node:
                yield from inorder(node.left)
                yield node.val
                yield from inorder(node.right)

        answer = current = TreeNode(None)
        for value in inorder(root):
            current.right = TreeNode(value)
            current = current.right
        return answer.right

    def increasingBST1(self, root: TreeNode) -> TreeNode:
        def inorder(node):
            if node:
                inorder(node.left)
                node.left = None
                self.current.right = node
                self.current = node
                inorder(node.right)

        answer = self.current = TreeNode(None)
        inorder(root)
        return answer.right


solution = Solution()
print(arr_from_btree(solution.increasingBST(deserialize([5, 3, 6, 2, 4, None, 8, 1, None, None, None, 7, 9]))))
