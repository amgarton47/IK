from Tree.Tree import *


# iterative
def search_node_in_bst(root, value):
    curr = root
    while curr:
        if curr.value == value:
            return True
        elif curr.value < value:
            curr = curr.right
        else:
            curr = curr.left

    return False


# recursive
def search_node_in_bst(root, value):
    if not root:
        return False
    elif root.value == value:
        return True
    elif root.value < value:
        return search_node_in_bst(root.right, value)
    else:
        return search_node_in_bst(root.left, value)


t1 = convert_arr_to_tree([30, 20, None, 10])
v1 = 5

output = search_node_in_bst(t1, v1)
expected1 = 0

print(f"Output: {output}", f"expected: {expected1}")
