def successor(root, k):
    if not root:
        return None

    # find minimum elt of right subtree
    if k.right:
        curr = k.right
        while curr.left:
            curr = curr.left

        return curr

    else:
        # find deepest left turn in tree, above node k
        ancestor = None
        curr = root
        while curr != k:
            if curr.value < k.value:
                curr = curr.right
            else:
                ancestor = curr
                curr = curr.left
        return ancestor


def predecessor(root, k):
    if not root:
        return None

    # find maximum elt of left subtree
    if k.left:
        curr = k.left
        while curr.left:
            curr = curr.left

        return curr
    else:
        # find deepest right turn in tree, above node k
        ancestor = None
        curr = root

        while curr != k:
            if curr.value < k.value:
                ancestor = curr
                curr = curr.right
            else:
                curr = curr.left

        return ancestor
