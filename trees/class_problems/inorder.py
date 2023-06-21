import sys

# adding Tree class and helpers to the system path
sys.path.insert(1, "/Users/aidangarton/Desktop/IK/trees/Tree")

from Tree import *


# recursive
def inorder(root):
    result = []

    def helper(root, ret):
        if not root:
            return

        helper(root.left, result)
        result.append(root.value)
        helper(root.right, result)

    helper(root, result)
    return result


# iterative
def inorder(root):
    node = root
    stack, result = [], []

    while stack or node:
        while node:
            stack.append(node)
            node = node.left

        node = stack.pop()
        result.append(node.value)
        node = node.right

    return result


arr = [0, 1, 2, 3, 4]
tree = convert_arr_to_tree(arr)

print(inorder(tree))
