import sys

# adding Tree class and helpers to the system path
sys.path.insert(1, "/Users/aidangarton/Desktop/IK/trees/Tree")

from Tree import *


# def build_binary_search_tree(preorder):
#     inorder = list(sorted(preorder))
#     return helper(preorder, inorder)


# def helper(preorder, inorder):
#     if len(preorder) == 0 or len(inorder) == 0:
#         return None

#     root = preorder[0]

#     if len(inorder) == 1:
#         return BinaryTreeNode(root)

#     boundary = binary_search(inorder, 0, len(inorder) - 1, root)

#     print("a", preorder, inorder, boundary, root)
#     print("b", inorder[:boundary], inorder[boundary + 1 :])

#     pre_idx = len(inorder[:boundary])

#     new_root = BinaryTreeNode(root)

#     new_root.left = helper(preorder[1 : pre_idx + 1], inorder[:boundary])
#     new_root.right = helper(preorder[pre_idx + 1 :], inorder[boundary + 1 :])

#     return new_root


def binary_search(arr, lo, hi, val):
    while lo <= hi:
        mid = (hi - lo) // 2 + lo

        if arr[mid] == val:
            return mid
        elif arr[mid] < val:
            lo = mid + 1
        else:
            hi = mid - 1

    return -1


def build_binary_search_tree(preorder):
    inorder = list(sorted(preorder))
    return helper(preorder, inorder, 0, len(inorder) - 1)


def helper(preorder, inorder, inorder_low, inorder_hi):
    if inorder_low > inorder_hi:
        return None

    root = preorder.pop(0)
    new_root = BinaryTreeNode(root)

    if inorder_low == inorder_hi:
        return new_root

    boundary = binary_search(inorder, inorder_low, inorder_hi, root)

    new_root.left = helper(preorder, inorder, inorder_low, boundary - 1)
    new_root.right = helper(preorder, inorder, boundary + 1, inorder_hi)

    return new_root


arr = [2, 0, 1, 3, 5, 4]
# arr = [0, -100, -90, 70, 20, 10, 100, 80]
# arr = [50, 90, 80, 85, 83]
tree = convert_arr_to_tree(arr)

out = build_binary_search_tree(arr)

print(out)
print(convert_tree_to_arr(out))
