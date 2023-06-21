# recursive
def postorder(root):
    result = []

    def helper(root, result):
        if not root:
            return

        helper(root.left, result)
        helper(root.right, result)
        result.append(root.value)

    helper(root, result)
    return result


# iterative
def postorder(root):
    stack = [root] if root else []
    result = []

    while stack:
        popped = stack.pop()
        result.append(popped.value)

        if popped.left:
            stack.append(popped.left)

        if popped.right:
            stack.append(popped.right)

    return result[::-1]
