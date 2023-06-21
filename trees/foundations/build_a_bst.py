from Tree.Tree import *


def build_a_bst(values):
    if len(values) == 0:
        return None

    root = BinaryTreeNode(values[0])

    for i in range(1, len(values)):
        insert_into_bst(root, values[i])

    return root


# iterative
def insert_into_bst(root, val):
    new_node = BinaryTreeNode(val)

    if not root:
        return new_node

    prev = None
    curr = root

    while curr:
        if curr.value == val:
            raise Exception("val is already present in the BST")
        elif curr.value < val:
            prev = curr
            curr = curr.right
        else:
            prev = curr
            curr = curr.left

    if prev.value < val:
        prev.right = new_node
    else:
        prev.left = new_node

    return root


# recursive
def insert_into_bst(root, val):
    if not root:
        return BinaryTreeNode(val)
    if root.value == val:
        raise Exception("val is already present in the BST")
    elif root.value < val:
        root.right = insert_into_bst(root.right, val)
    else:
        root.left = insert_into_bst(root.left, val)

    return root


vals = [7, 5, 9]

bst = build_a_bst(vals)
