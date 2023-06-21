from build_a_bst import build_a_bst


# iterative
def get_maximum_value(root):
    if not root:
        return None

    while root.right:
        root = root.right

    return root.value


# recursive
def get_maximum_value(root):
    if not root:
        return None
    if root.right:
        return get_maximum_value(root.right)
    else:
        return root.value


t1 = build_a_bst([30, 20, 10])
print(get_maximum_value(t1))
