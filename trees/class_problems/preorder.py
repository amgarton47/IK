import sys

# adding Tree class and helpers to the system path
sys.path.insert(1, "/Users/aidangarton/Desktop/IK/trees/Tree")

from Tree import *


# recursive
def preorder(root):
    result = []

    def helper(root, ret):
        if not root:
            return

        result.append(root.value)
        helper(root.left, result)
        helper(root.right, result)

    helper(root, result)
    return result


# iterative
def preorder(root):
    if not root:
        return []

    result = []

    stack = [root]
    while stack:
        popped = stack.pop()
        result.append(popped.value)

        if popped.right:
            stack.append(popped.right)

        if popped.left:
            stack.append(popped.left)
    return result


arr = [0, 1, 2, 3, 4]
tree = convert_arr_to_tree(arr)

print(preorder(tree))
