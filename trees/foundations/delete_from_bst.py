def delete(root, k):
    # first search for k in tree
    curr = root
    prev = None
    while curr:
        if curr.value == k:
            break
        elif curr.value < k:
            prev = curr
            curr = curr.right
        else:
            prev = curr
            curr = curr.left

    # if k not found in tree, return tree as is
    if not curr:
        return root

    # case 1: k is a leaf (has 0 children)
    if curr.left == curr.right == None:
        if not prev:  # edge case where k is the only node in the tree
            return None
        if prev.left == curr:
            prev.left = None
        else:  # prev.right.value == k
            prev.right = None

        return root

    # case 2: k has one child
    child = None

    if curr.right and not curr.left:
        child = curr.right

    if curr.left and not curr.right:
        child = curr.left

    if child:
        if prev == None:  # edge case where node k is root
            root = child
            return root

        if prev.left == curr:
            prev.left = child
        else:  # prev.right.value == curr.value
            prev.right = child

        return root

    # case 3: k has two children
    if curr.left and curr.right:
        successor = curr.right
        prev = curr

        while successor.left:
            prev = successor
            successor = successor.left

        # copy successor value into curr node
        curr.value = successor.value

        # then delete successor node which now holds val of curr
        if successor == prev.left:
            prev.left = successor.right
        else:  # successor == prev.right
            prev.right = successor.right

        return root
