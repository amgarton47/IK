import sys

# adding Tree class and helpers to the system path
sys.path.insert(1, "/Users/aidangarton/Desktop/IK/trees/Tree")

from Tree import *


def flip_upside_down(root):
    if not root:
        return None

    if not root.right and not root.left:
        return root  # new root

    new_root = flip_upside_down(root.left)

    root.left.left = root.right
    root.left.right = root

    root.left = None
    root.right = None

    return new_root


arr = [1, 2, 3, 4, 5, None, None, 6, 7]
# arr = [9295, 7197, 7032, 49, 9092]
tree = convert_arr_to_tree(arr)

out = flip_upside_down(tree)
