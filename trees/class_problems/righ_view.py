# return list of right most element in each level by traversing level by level
def right_view(root):
    if not root:
        return []

    result = []
    stack = [root]

    while stack:
        lngth = len(stack)
        for i in range(lngth):
            popped = stack.pop(0)

            if i == lngth - 1:
                result.append(popped.value)
            if popped.left:
                stack.append(popped.left)
            if popped.right:
                stack.append(popped.right)

    return result
