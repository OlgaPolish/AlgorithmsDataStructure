class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def calculate_sum(self):
        left_sum = self.left.data if self.left else 0
        right_sum = self.right.data if self.right else 0
        return left_sum, right_sum,


def sum_tree(node):
    if node is None:
        return 0
    return node.data + sum_tree(node.left) + sum_tree(node.right)


def is_sum_tree(node):
    if node is None or (node.left is None and node.right is None):
        return 1

    left_sum = sum_tree(node.left) if node.left else 0
    right_sum = sum_tree(node.right) if node.right else 0

    if node.data == left_sum + right_sum:
        return is_sum_tree(node.left) and is_sum_tree(node.right)

    return 0


def print_tree(node):
    if node is None:
        return
    print(
        f"Node {node.data}: left -> {node.left.data if node.left else None},\
         right -> {node.right.data if node.right else None}")
    print_tree(node.left)
    print_tree(node.right)


root = Node(26)
root.left = Node(10)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(6)
root.right.right = Node(3)

print_tree(root)

left_sum, right_sum = root.calculate_sum()
print(f"Сумма левого поддерева: {left_sum}")
print(f"Сумма правого поддерева: {right_sum}")

print(is_sum_tree(root))
