import sys

# adding Tree class and helpers to the system path
sys.path.insert(1, "/Users/aidangarton/Desktop/IK/trees/Tree")

from Tree import *


# iterative, not grouping by level
def level_order_traversal(root):
    if not root:
        return []

    q = [root]
    result = []

    while q:
        popped = q.pop(0)

        if popped.left:
            q.append(popped.left)

        if popped.right:
            q.append(popped.right)

        result.append(popped.value)

    return result


# iterative, grouping by level
def level_order_traversal(root):
    if not root:
        return []

    q = [root]
    result = []

    while q:
        temp = []

        for _ in range(len(q)):
            popped = q.pop(0)

            if popped.left:
                q.append(popped.left)

            if popped.right:
                q.append(popped.right)

            temp.append(popped.value)
        result.append(temp)

    return result


# recursive, grouping by level
def level_order_traversal(root):
    ret = []

    def recursive_helper(root, level, ret):
        if not root:
            return

        if level >= len(ret):
            ret.append([])

        ret[level].append(root.value)

        recursive_helper(root.left, level + 1, ret)
        recursive_helper(root.right, level + 1, ret)

    recursive_helper(root, 0, ret)
    return ret


# level order traversal for n-ary trees, grouping by level
def n_ary_level_order_traversal(root):
    if not root:
        return []

    q = [root]
    result = []

    while q:
        temp = []
        for _ in range(len(q)):
            popped = q.pop(0)
            for child in popped.children:
                q.append(child)

            temp.append(popped.value)

        result.append(temp)

    return result


def zigzag_level_order_traversal(root):
    if not root:
        return []

    result = []
    q = [root]
    left_to_right = True

    while q:
        q_lngth = len(q)
        temp = [0] * q_lngth

        for i in range(len(q)):
            idx = i if left_to_right else q_lngth - i - 1
            popped = q.pop(0)

            if popped.left:
                q.append(popped.left)

            if popped.right:
                q.append(popped.right)

            temp[idx] = popped.value

        left_to_right = not left_to_right
        result.append(temp)

    return result


# standard level order traversal test

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, None, None, 10, 11, None, None]
tree = convert_arr_to_tree(arr)

# print(level_order_traversal(tree))
print(zigzag_level_order_traversal(tree))


# n-ary traversal test

# class NaryTreeNode:
#     def __init__(self, value):
#         self.value = value
#         self.children = []

# root = NaryTreeNode(1)
# lvl1 = [NaryTreeNode(3), NaryTreeNode(2), NaryTreeNode(4)]
# lvl2 = [NaryTreeNode(5), NaryTreeNode(6)]

# root.children = lvl1
# lvl1[0].children = lvl2

# print(n_ary_level_order_traversal(root))
