import sys

# adding Tree class and helpers to the system path
sys.path.insert(1, "/Users/aidangarton/Desktop/IK/trees/Tree")

from Tree import *


def level_order_traversal(root):
    if not root:
        return []

    result = []
    q = [root]

    while q:
        temp = []

        for _ in range(len(q)):
            popped = q.pop(0)
            temp.append(popped.value)

            if popped.left:
                q.append(popped.left)

            if popped.right:
                q.append(popped.right)
        result.append(temp)

    return result


def level_order(root):
    if not root:
        return []

    result = []
    q = [root]

    while q:
        temp = []

        for _ in range(len(q)):
            popped = q.pop(0)
            temp.append(popped.value)

            for child in popped.children:
                q.append(child)

        result.append(temp)

    return result


# convert linked list to height balanced BST
def sorted_list_to_bst(head):
    # below is commented out for when input is arr instead of linked list
    arr = []

    while head:
        arr.append(head.value)
        head = head.next

    hi = len(arr) - 1
    lo = 0

    root = helper(arr, lo, hi)
    return root


def helper(arr, lo, hi):
    if lo > hi:
        return None

    mid = (hi - lo) // 2 + lo

    root = BinaryTreeNode(arr[mid])

    root.left = helper(arr, lo, mid - 1)
    root.right = helper(arr, mid + 1, hi)

    return root


def all_paths_sum_k(root, k):
    result = []
    helper([], root, result, k)
    return result if len(result) > 0 else [[-1]]


def helper(slate, root, result, k):
    # at leaf node, path is done, so check if path has summed to k
    if not root.left and not root.right:
        if k == root.value:
            slate.append(root.value)
            result.append(slate[:])
            slate.pop()
        return

    slate.append(root.value)

    if root.left:
        helper(slate, root.left, result, k - root.value)

    if root.right:
        helper(slate, root.right, result, k - root.value)

    slate.pop()


arr = [-1, 2, 3, 5, 6, 7, 10]

# out = sorted_list_to_bst(arr)

# print(convert_tree_to_arr(out))

tree = convert_arr_to_tree(arr)

print(all_paths_sum_k(tree, 6))
