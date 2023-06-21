# naive solution is to generate all paths that sum to k and return true if any were found, false otherwise
def path_sum(root, k):
    result = []
    helper([], root, result, k)
    return True if len(result) else False


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


# backtracking / optimized approach
# stop if a path has been found
def path_sum(root, k):
    result = []
    helper([], root, result, k)
    return True if len(result) else False


def helper(slate, root, result, k):
    # at leaf node, path is done, so check if path has summed to k
    if not root.left and not root.right:
        return k == root.value

    slate.append(root.value)

    l = r = False
    if root.left:
        l = helper(slate, root.left, result, k - root.value)

    if root.right:
        r = helper(slate, root.right, result, k - root.value)

    return l or r
