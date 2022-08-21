class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None

    def add_node(self, val):
        def dfs(node):
            if not node:
                return TreeNode(val)

            if val >= node.val:
                node.right = dfs(node.right)
            else:
                node.left = dfs(node.left)
            return node

        self.root = dfs(self.root)

    def add_nodes(self, values):
        for val in values:
            self.add_node(val)

    def for_each_node(self, func):
        def dfs(node):
            if not node:
                return None
            func(node)
            dfs(node.left)
            dfs(node.right)
            return node

        dfs(self.root)
        return self

    def reduce(self, reducer, start_value=0):
        def dfs(node, accumulator):
            if not node:
                return accumulator

            return reducer(node, dfs(node.left, accumulator), dfs(node.right, accumulator))
        return dfs(self.root, start_value)


tree = BinarySearchTree()
tree.add_nodes([40, 20, 60, 10, 30, 50, 70])

print("Print all values")
print('-----------')

def print_node(node):
    print(node.val)


tree.for_each_node(print_node)

print("\nInvert the binary tree")
print('-----------')

def invert(node):
    node.left, node.right = node.right, node.left


tree.for_each_node(invert).for_each_node(print_node)

print("\nUsing reduce")
print('-----------')

def height(_, left, right):
    return max(left, right) + 1


def count(_, left, right):
    return 1 + left + right


def sum_total(node, left, right):
    return node.val + left + right


def left_width(_, left, right):
    return min(left - 1, right + 1)


def right_width(_, left, right):
    return max(left - 1, right + 1)


def to_array(node, left, right):
    return left + [node.val] + right


print("Height:", tree.reduce(height))
print("Count:", tree.reduce(count))
print("Sum:", tree.reduce(sum_total))
print("Width:", tree.reduce(right_width) - tree.reduce(left_width))
print("Arr:", tree.reduce(to_array, []))
