import sys

# adding Tree class and helpers to the system path
sys.path.insert(1, "/Users/aidangarton/Desktop/IK/trees/Tree")

from Tree import *


# return the diameter of the binary tree rooted at root
# the diameter of a binary tree is the longest path from any two nodes in the tree
# note: the longest path between two nodes in a binary tree does NOT necessarily pass through the root
def binary_tree_diameter(root):
    global global_diameter
    global_diameter = 0

    def helper(root):
        if not root:
            return 0

        if not root.left and not root.right:
            return 0

        left_max = right_max = 0

        if root.left:
            left_max = helper(root.left) + 1
        if root.right:
            right_max = helper(root.right) + 1

        local_diameter = left_max + right_max

        global global_diameter
        global_diameter = max(global_diameter, local_diameter)
        return max(left_max, right_max)

    helper(root)
    return global_diameter


arr = [0, 1, None, 2, 3, 4, None, None, 5]
tree = convert_arr_to_tree(arr)

print(binary_tree_diameter(tree))
