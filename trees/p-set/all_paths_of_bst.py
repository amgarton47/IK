import sys

# adding Tree class and helpers to the system path
sys.path.insert(1, "/Users/aidangarton/Desktop/IK/trees/Tree")

from Tree import *


def all_paths_of_a_binary_tree(root):
    if not root:
        return []

    ret = []
    helper(root, ret, [])
    return ret


def helper(root, ret, slate):
    if not root.left and not root.right:
        slate.append(root.value)
        ret.append(slate[:])
        slate.pop()
        return

    slate.append(root.value)

    if root.left:
        helper(root.left, ret, slate)

    if root.right:
        helper(root.right, ret, slate)

    slate.pop()


arr = [1, 2, 3, 4, 5, 6, 7]
tree = convert_arr_to_tree(arr)

print(all_paths_of_a_binary_tree(tree))
