class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def convert_arr_to_tree(arr):
    return arr_to_tree_helper(arr, 0, len(arr))


def arr_to_tree_helper(arr, i, n):
    root = None

    if i < n:
        root = BinaryTreeNode(arr[i])

        root.left = arr_to_tree_helper(arr, 2 * i + 1, n)
        root.right = arr_to_tree_helper(arr, 2 * i + 2, n)

    return root


def convert_tree_to_arr(root):
    arr = []
    tree_to_arr_helper(root, arr)
    return arr


def tree_to_arr_helper(root, arr):
    if not root:
        return None

    q = [root]
    while q:
        popped = q.pop(0)
        arr.append(popped.value)

        if popped.left:
            q.append(popped.left)

        if popped.right:
            q.append(popped.right)
