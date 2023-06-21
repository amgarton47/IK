# initial solution
def kth_smallest_element(root, k):
    trav = []
    inorder(root, trav)

    return trav[k - 1]


def inorder(root, ret):
    if not root:
        return

    inorder(root.left, ret)
    ret.append(root.value)
    inorder(root.right, ret)


# solution that implements backtracking
def kth_smallest_element(root, k):
    global idx
    idx = 1
    val = 0

    def inorder(root, k):
        if not root or idx <= 0:
            return

        inorder(root.left, k)
        idx -= 1
        if idx == k:
            global val
            val = root.value

        inorder(root.right, k)

    inorder(root, k)
    return val


bst = []
