class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


def identicalTrees(a, b):
    if a is None and b is None:
        return True
    if a is None or b is None:
        return False
    return (a.data == b.data) and identicalTrees(a.left, b.left) and identicalTrees(a.right, b.right)


root_a = Node(1)
root_a.left = Node(2)
root_a.right = Node(3)
root_a.left.left = Node(4)
root_a.left.right = Node(5)

root_b = Node(1)
root_b.left = Node(2)
root_b.right = Node(3)
root_b.left.left = Node(4)
root_b.left.right = Node(5)

root_c = Node(1)
root_c.left = Node(3)
root_c.right = Node(2)
root_c.left.left = Node(5)

print(identicalTrees(root_a, root_b))
print(identicalTrees(root_a, root_c))
